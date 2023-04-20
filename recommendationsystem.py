# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

def process_chunk(chunk, user, recommendations):
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(chunk["Title"])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    for idx, row in chunk.iterrows():
        if row["Uploader"] == user:
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:6]

            for video, score in sim_scores:
                title = chunk.iloc[video]["Title"]
                recommendations[title] += 1

users = ["Dhruv", "Ron", "Inbar", "Daniel", "Mor", "Guy", "Memi"]

for user in users:
    print(f"Top 3 recommendations for {user}:")
    recommendations = defaultdict(int)

    for i in range(1, 6):
        chunk = pd.read_csv(f"dataset_{i}.csv")
        process_chunk(chunk, user, recommendations)

    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    top_recommendations = [video[0] for video in sorted_recommendations[:3]]

    print(top_recommendations)
    print()

import matplotlib.pyplot as plt

# Load all datasets and concatenate them
dfs = [pd.read_csv(f"dataset_{i}.csv") for i in range(1, 6)]
df = pd.concat(dfs, ignore_index=True)

# Group by title and calculate the sum of hours watched
grouped_df = df.groupby("Title")["Hours_Played"].sum().reset_index()

# Sort by hours watched
sorted_df = grouped_df.sort_values("Hours_Played", ascending=False)

# Plot the histogram
plt.figure(figsize=(12, 6))
plt.bar(sorted_df["Title"].head(10), sorted_df["Hours_Played"].head(10))
plt.xlabel("Video Title")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Number of Hours Watched")
plt.title("Top 10 Video Titles vs. Number of Hours Watched")
plt.show()

