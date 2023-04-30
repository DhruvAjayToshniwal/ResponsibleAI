import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
import matplotlib.pyplot as plt

def process_chunk(chunk, user, recommendations):
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(chunk["Title"])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    for idx, row in chunk.iterrows():
        if row["User"] == user:
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:6]

            for video, score in sim_scores:
                title = chunk.iloc[video]["Title"]
                engagement_score = (chunk.iloc[video]["UserTime"] * (chunk.iloc[video]["Likes"] + chunk.iloc[video]["Shares"] - chunk.iloc[video]["Dislikes"])) + chunk.iloc[video]["Comments"] + chunk.iloc[video]["ViewCount"]
                recommendations[title] += engagement_score * chunk.iloc[video]["NumberOfTimesWatched"]

users = ["Dhruv", "Ron", "Inbar", "Daniel", "Mor", "Guy", "Memi", "Giulia"]

# Create a dictionary to store the total engagement score for each user for each day
user_engagement = defaultdict(list)

for i in range(1, 6):
    print(f"\nDay {i} recommendations:")
    for user in users:
        print(f"\nTop 3 recommendations for {user}:")
        recommendations = defaultdict(int)

        chunk = pd.read_csv(f"dataset_{i}.csv")
        process_chunk(chunk, user, recommendations)

        sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        top_recommendations = [video[0] for video in sorted_recommendations[:3]]
        
        print(top_recommendations)

        # add the total engagement score of the top 3 recommendations for the user for the day
        user_engagement[user].append(sum([recommendations[video] for video in top_recommendations]))
