import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

random.seed(1)

def create_dataset(file_number, users, video_types, video_challenges, video_uploaders):
    data = []
    for _ in range(1000):
        user = random.choice(users)
        video_type = random.choice(video_types)
        uploader = random.choice(video_uploaders)

        if user == "Giulia" and random.random() < 0.9:
            video_title = f"Condom Challenge by {uploader}"
        elif user == "Christopher" and random.random() < 0.7:
            video_title = f"Hot Pepper Challenge by {uploader}"
        elif video_type == "Challenge":
            video_title = f"{random.choice(video_challenges)} by {uploader}"
        else:
            video_title = f"{video_type} video by {uploader}"

        duration = random.randint(1, 120)
        view_count = random.randint(1000, 100000)
        num_watched = random.choices([1, 2, 3, 4, 5], weights=[0.9, 0.025, 0.025, 0.025, 0.025])[0]
        user_time = random.randint(1, min(duration * num_watched, 180))
        likes = random.randint(0, view_count)
        dislikes = random.randint(0, view_count)
        comments = random.randint(0, view_count)
        shares = random.randint(0, comments)

        data.append([user, video_title, duration, view_count, user_time, num_watched, likes, dislikes, shares, comments])

    df = pd.DataFrame(data, columns=["User", "Title", "Duration", "ViewCount", "UserTime", "NumberOfTimesWatched", "Likes", "Dislikes", "Shares", "Comments"])
    df.to_csv(f"dataset_{file_number}.csv", index=False)

def initialize_user_profiles(users):
    return {user: [] for user in users}

def process_chunk(chunk, user_profiles, users):
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(chunk["Title"])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    most_watched_keywords = defaultdict(list)
    for user, user_chunk in chunk.groupby("User"):
        user_profiles[user] = get_top_recommendations(user_chunk, cosine_sim)
        most_watched_keywords[user] = user_chunk["Title"].head(5).tolist()
    return user_profiles, most_watched_keywords

def get_top_recommendations(user_chunk, cosine_sim):
    recommendations = []

    for idx, row in user_chunk.iterrows():
        sim_scores = sorted(list(enumerate(cosine_sim[idx])), key=lambda x: x[1], reverse=True)[1:11]

        for video, score in sim_scores:
            title = chunk.iloc[video]["Title"]  # Change this line
            engagement_score = calculate_engagement_score(chunk.iloc[video])  # Change this line
            recommendations.append((title, engagement_score))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return remove_duplicates(recommendations)[:5]

def calculate_engagement_score(row):
    return (row["UserTime"] * (row["Likes"] + row["Shares"] - row["Dislikes"])) + row["Comments"] + row["ViewCount"]

def remove_duplicates(recommendations):
    seen = set()
    unique_recommendations = [rec for rec in recommendations if not (rec[0] in seen or seen.add(rec[0]))]
    return unique_recommendations

users = ["Dhruv", "Ron", "Inbar", "Daniel", "Mor", "Guy", "Memi", "Giulia", "Christopher"]
video_types = ["Csgo", "Music", "Csgo", "Football", "Cooking", "Football", "Chess", "Fashion", "Beauty", "Documentary", "Education", "DIY", "Talk show", "Car review", "Animal", "Art", "News", "Fitness", "Product unboxing", "Yoga"]
video_challenges = ["Ice Bucket Challenge", "Cinnamon Challenge", "Condom Challenge", "Mannequin Challenge", "Hot Pepper Challenge", "Try Not to Laugh Challenge", "Whisper Challenge"]
video_uploaders = ["Pewdiepie", "Nelk Boys", "Joe Rogan", "Agadmator", "Sean"]

for i in range(1, 6):
    create_dataset(i, users, video_types, video_challenges, video_uploaders)

user_profiles = initialize_user_profiles(users)

for i in range(1, 6):
    print(f"\nDay {i} recommendations:")
    chunk = pd.read_csv(f"dataset_{i}.csv")
    user_profiles, most_watched_keywords = process_chunk(chunk, user_profiles, users)

    for user in users:
        print(f"\nTop 5 recommendations for {user}:")
        print([video[0] for video in user_profiles[user]])
        print(f"Most watched video keywords for {user}:")
        print(most_watched_keywords[user])
