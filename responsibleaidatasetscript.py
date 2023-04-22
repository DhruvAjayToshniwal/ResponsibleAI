import pandas as pd
import numpy as np
import random
import math

def create_dataset(file_number):
    users = ["Dhruv", "Ron", "Inbar", "Daniel", "Mor", "Guy", "Memi", "Giulia"]
    video_types = ["Csgo", "Music", "Csgo", "Football", "Cooking", "Football", "Chess", "Fashion", "Beauty", "Documentary", "Education", "DIY", "Talk show", "Car review", "Animal", "Art", "News", "Fitness", "Product unboxing", "Yoga"]
    video_challenges = ["Ice Bucket Challenge", "Cinnamon Challenge", "Condom Challenge", "Mannequin Challenge", "Hot Pepper Challenge", "Try Not to Laugh Challenge", "Whisper Challenge"]
    video_genres = video_types + video_challenges
    video_uploaders = ["Pewdiepie", "Nelk Boys", "Joe Rogan", "Agadmator", "Sean"]

    data = []
    for _ in range(15000):
        user = random.choice(users)
        video_type = random.choice(video_types)
        uploader = random.choice(video_uploaders)

        if user == "Giulia":
            if random.random() < 0.7:
                video_title = f"Condom Challenge by {uploader}"
            else:
                if video_type == "Challenge":
                    video_title = f"{random.choice(video_challenges)} by {uploader}"
                else:
                    video_title = f"{video_type} video by {uploader}"
        else:
            if video_type == "Challenge":
                video_title = f"{random.choice(video_challenges)} by {uploader}"
            else:
                video_title = f"{video_type} video by {uploader}"

        duration = random.randint(1, 60) # in minutes
        view_count = random.randint(1000, 100000)
        num_watched = random.choices([1, 2, 3, 4, 5], weights=[0.9, 0.025, 0.025, 0.025, 0.025])[0]
        user_time = random.randint(math.ceil(duration * 0.3), duration*num_watched) # in minutes
        likes = random.randint(0, view_count)
        dislikes = random.randint(0, view_count)
        comments = random.randint(0, view_count)
        shares = random.randint(0, comments)

        data.append([user, video_title, duration, view_count, user_time, num_watched, likes, dislikes, shares, comments])

    df = pd.DataFrame(data, columns=["User", "Title", "Duration", "ViewCount", "UserTime", "NumberOfTimesWatched", "Likes", "Dislikes", "Shares", "Comments"])
    df.to_csv(f"dataset_{file_number}.csv", index=False)

for i in range(1, 6):
    create_dataset(i)
