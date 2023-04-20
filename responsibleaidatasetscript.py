import csv
import random
import pandas as pd

platforms = ["YouTube", "TikTok"]
challenge_titles = [
    "Condom Snorting Challenge",
    "The Fire Challenge",
    "Tide Pod Eating Challenge",
    "Inhaling Cinnamon Challenge",
    "Hot Coil Challenge",
    "Choking Game Challenge",
    "Drinking Boiling Water Challenge",
    "The Deodorant Challenge",
    "Salt and Ice Challenge",
    "The Duct Tape Challenge",
]

normal_titles = [
    "Chess Strategy for Beginners",
    "CS:GO - Best Tips and Tricks",
    "Top 10 Pop Music Hits",
    "How to Play Guitar - Beginner Lesson",
    "Meditation for Stress Relief",
    "Yoga for Flexibility and Strength",
    "Photography Tips for Stunning Photos",
    "Basic Cooking Techniques for Beginners",
    "Travel Guide: Top 10 Places to Visit",
    "DIY Home Decoration Ideas",
]

users = ["Dhruv", "Ron", "Inbar", "Daniel", "Mor", "Guy", "Memi"]

def generate_data(file_number):
    data = []
    for i in range(1, 9001):
        platform = random.choice(platforms)
        uploader = random.choice(users)
        view_count = random.randint(10000, 5000000)
        likes = random.randint(1000, 150000)
        dislikes = random.randint(500, 50000)
        duration = random.randint(1, 60)
        hours_played = round(view_count * duration * random.uniform(0.0001, 0.0002), 2)

        if i % file_number == 0 and uploader == "Mor":
            title = "Condom Snorting Challenge"
        elif i % file_number == 0:
            title = random.choice(challenge_titles)
        else:
            title = random.choice(normal_titles)

        data.append(
            [i, platform, f"{title} - {platform}", uploader, view_count, likes, dislikes, duration, hours_played]
        )
    return data

def write_csv(data, filename="dataset.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Video_ID", "Platform", "Title", "Uploader", "View_Count", "Likes", "Dislikes", "Duration", "Hours_Played"])
        writer.writerows(data)

if __name__ == "__main__":
    for i in range(1, 6):
        data = generate_data(i)
        write_csv(data, f"dataset_{i}.csv")
