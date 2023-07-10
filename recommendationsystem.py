For this code, write another blog.

import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

users = ["Dhruv", "Inbar", "Roni", "Daniel", "Guy", "Memi", "Mor", "Christopher", "Giulia"]
video_types = ["Tutorial", "Music", "News", "Comedy","Podcasts","Pranks","ASMR","Compilations","Gaming","Travel"]
video_challenges = ["Ice Bucket Challenge","Mannequin Challenge","Try Not To Laugh Challenge","Condom Challenge"]
video_uploaders = [ "Sean", "Mr Beast", "The Baby", "Capibara","Bibi","Haya","Jazza","Kurtis","Boris","Rihanna"]
challenge_video_uploaders = ["Pewdiepie", "Nelk Boys", "Joe Rogan", "Agadmator","Opal","Alon"]

random.seed(42)

def initialize_user_profiles(users):
    return {user: [] for user in users}

from itertools import product

videos=[]

for video in list(product(video_types, video_uploaders)):
  # if video[0] == "Challenge":
  #     video_title = f"{random.choice(video_challenges)} by {video[1]}"
  # else:
  video_title = f"{video[0]} video by {video[1]}"
  duration = random.randint(1, 120)
  view_count = random.randint(1000, 100000)
  likes = random.randint(0, view_count)
  dislikes = random.randint(0, view_count)
  comments = random.randint(0, view_count)
  shares = random.randint(0, comments)
  videos.append([video_title,duration, view_count, likes, dislikes, shares, comments])

for video in list(product(video_challenges, challenge_video_uploaders)):
  # if video[0] == "Challenge":
  #     video_title = f"{random.choice(video_challenges)} by {video[1]}"
  # else:
  video_title = f"{video[0]} video by {video[1]}"
  duration = random.randint(1, 120)
  view_count = random.randint(1000, 100000)
  likes = random.randint(0, view_count)
  dislikes = random.randint(0, view_count)
  comments = random.randint(0, view_count)
  shares = random.randint(0, comments)
  videos.append([video_title,duration, view_count, likes, dislikes, shares, comments])

import re

def process_chunk(user_profiles,i,recommendations):
    data = []
    for _ in range(100):
        user = random.choice(users)
        if i==1:
          video = random.choice(videos)
        else:
          if random.random()<0.7:
            video = random.choice(recommendations[i][recommendations[i]["User"]==user].drop(columns=["User","UserTime", "NumberOfTimesWatched"]).drop_duplicates().values)
          else:
            video = random.choice(videos)
          # print (video)
        if user == "Giulia" and re.split("video",video[0])[0].strip() in video_challenges[:2]:
            num_watched = 4
        elif user == "Giulia" and re.split("video",video[0])[0].strip() == video_challenges[3]:
            user = random.choice(users[:7])
            num_watched = random.choices([0, 1, 2, 3, 4], weights=[0.025, 0.9, 0.025, 0.025, 0.025])[0]
        else:
            num_watched = random.choices([0, 1, 2, 3, 4], weights=[0.025, 0.9, 0.025, 0.025, 0.025])[0]

        user_time = random.randint(0, min(video[1] * num_watched, 180))
        # if "Challenge" in video[0]:
        #   genre="Challenge"
        # else:
        genre=re.split(" video",video[0])[0]
        uploader=re.split(" by ",video[0])[1]
        data.append([user, video[0], video[1], video[2], user_time, num_watched, video[3], video[4], video[5], video[6],genre,uploader])

    chunk = pd.DataFrame(data, columns=["User", "Title", "Duration", "ViewCount", "UserTime", "NumberOfTimesWatched", "Likes", "Dislikes", "Shares", "Comments","Genre","Uploader"])

    # print(chunk)

    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(chunk["Title"])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    most_watched_keywords = defaultdict(list)
    f=0
    recommended="empty"
    for user, user_chunk in chunk.groupby("User"):
        seen_titles = set(user_chunk["Title"].tolist())
        user_profiles[user], seen_titles = get_top_recommendations(user_chunk, cosine_sim, seen_titles, chunk)
        most_watched_keywords[user] = user_chunk.nlargest(5, 'NumberOfTimesWatched')["Title"].tolist()

        # Update user_chunk with recommendations
        recommended_titles = [video[0] for video in user_profiles[user]]
        recommended_rows = chunk[chunk["Title"].isin(recommended_titles)].copy()
        recommended_rows["User"] = user
        if f!=0:
          recommended=pd.concat([recommended,recommended_rows])
        else:
          f=1
          recommended=recommended_rows

    return user_profiles, most_watched_keywords, chunk, recommended



def calculate_engagement_score(row):
    likes_weight = 0.4
    dislikes_weight = 0.1
    shares_weight = 0.3
    comments_weight = 0.2
    engagement_score = ((row["Likes"] * likes_weight) - (row["Dislikes"] * dislikes_weight) + (row["Shares"] * shares_weight) + (row["Comments"] * comments_weight))
    return engagement_score


def get_top_recommendations(user_chunk, cosine_sim, seen_titles, chunk):
    recommendations = []
    for idx, row in user_chunk.nlargest(5, 'NumberOfTimesWatched').iterrows():
        sim_scores = sorted(list(enumerate(cosine_sim[idx])), key=lambda x: x[1], reverse=True)[1:11]

        for video, score in sim_scores:
            title = chunk.iloc[video]["Title"]
            if title not in seen_titles:
                engagement_score = calculate_engagement_score(chunk.iloc[video])
                recommendations.append((title, engagement_score))
                seen_titles.add(title)

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:9], seen_titles

def analyze_results(user_profiles, most_watched_keywords, users, day):
    print(f"Day {day}:")
    for user in users:
        print(f"\n{user}:")
        print(f"Top 5 Most Watched Videos:")
        seen_titles = set()
        for title in most_watched_keywords[user]:
            if title not in seen_titles:
                print(f"{len(seen_titles) + 1}. {title}")
                seen_titles.add(title)
            if len(seen_titles) >= 5:
                break
        print("\nRecommendations:")
        seen_recommendations = set()
        for title, _ in user_profiles[user]:
            if title not in seen_recommendations:
                print(f"{len(seen_recommendations) + 1}. {title}")
                seen_recommendations.add(title)
            if len(seen_recommendations) >= 5:
                break
    print("\n" + "="*50 + "\n")


giulia_progress = []
christopher_progress = []
engagement_score_over_time = defaultdict(list)
user_engagement_over_time = defaultdict(list)
video_views_over_time = {'Total': []}
unique_video_types_over_time = defaultdict(list)
dangerous_recommended = defaultdict(list)
dangerous_watched = defaultdict(list)
recommendation={}
chunks={}

for i in range(1, 10):
  user_profiles = initialize_user_profiles(users)
  user_profiles, most_watched_keywords, chunk, recommended = process_chunk(user_profiles,i,recommendation)
  recommendation[i+1]=recommended
  analyze_results(user_profiles, most_watched_keywords, users, i)


  for user in users:
      user_chunk = chunk[chunk["User"] == user]
      user_rec=recommended[recommended["User"] == user]
      engagement_scores = user_chunk.apply(calculate_engagement_score, axis=1)
      engagement_score_over_time[user].append(np.mean(engagement_scores))
      user_engagement_over_time[user].append(user_chunk["NumberOfTimesWatched"].sum())
      unique_video_types_over_time[user].append(user_chunk["Genre"].nunique())
      if user=="Giulia":
        dangerous_watched[user].append(user_chunk[user_chunk["Genre"]=="Condom Challenge"].shape[0])
        dangerous_recommended[user].append(user_rec[user_rec["Genre"]=="Condom Challenge"].shape[0])
  chunks[i]=chunk

  video_views_over_time['Total'].append(chunk["ViewCount"].sum())

def var_of_vids(sentences):
    # Step 1: Create vocabulary - a set of distinct tokens from your input sentences
    vocab = set()
    for sentence in sentences:
        tokens = sentence.split()
        for token in tokens:
            vocab.add(token)

    # Step 2: Create a map (token: ID)
    vocab_map = {}
    for i, token in enumerate(sorted(vocab)): # sorted lexicographically for reproducibility
        vocab_map[token] = i

    vectors=[]
    # encode the sentences using the map you created in the previous step
    for sentence in sentences:
        encoded_sentence = []
        tokens = sentence.split()
        for token in tokens:
            encoded_sentence.append(vocab_map[token])
        if encoded_sentence[-4:][0]==17:
          vectors.append([encoded_sentence[-5:][:4][0],encoded_sentence[-5:][:4][-1]])
        else:
          vectors.append([encoded_sentence[-4:][0],encoded_sentence[-4:][-1]])
        # vectors.append(encoded_sentence)
    return vectors

var_start=[]
for user in users:
  vec=var_of_vids(recommendation[2][recommendation[2]["User"]==user]["Title"])
  var_start.append(np.var(vec)/len(vec))
print("mean variance in recommendations in the start of simulation: ",np.mean(var_start))

var_end=[]
for user in users:
  vec=var_of_vids(recommendation[10][recommendation[10]["User"]==user]["Title"])
  var_end.append(np.var(vec)/len(vec))
print("mean variance in recommendations in the end of simulation:",np.mean(var_end))

print("diffrence in variance for each user: ",np.array(var_start)-np.array(var_end))
print("mean diffrence in variance for each user: ",np.mean(np.array(var_start)-np.array(var_end)))

all_var=[]
var=[]
for i in range(2,11):
  for user in users:
    vec=var_of_vids(recommendation[i][recommendation[i]["User"]==user]["Title"])
    var.append(np.var(vec)/len(vec))
  all_var.append(np.mean(np.array(var)))
