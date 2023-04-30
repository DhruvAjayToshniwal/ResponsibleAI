# Plot the total engagement score of the recommendations for each user for each day
for user, engagement in user_engagement.items():
    plt.plot(range(1, 6), engagement, marker='o', label=user)

plt.xlabel('Day')
plt.ylabel('Total Engagement Score of Recommendations')
plt.title('Total Engagement Score of Recommendations for each User over Days')
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

# read in the dataset
df = pd.concat([pd.read_csv(f"dataset_{i}.csv") for i in range(1, 6)])

# create a dictionary of engagement time by user
engagement_time = defaultdict(int)

users = ["Dhruv", "Ron", "Inbar", "Daniel", "Mor", "Guy", "Memi", "Giulia"]
recommended_videos = {}

for user in users:
    recommendations = defaultdict(int)
    user_df = df[df['User'] == user]
    
    # Get recommended videos first
    for idx, row in user_df.iterrows():
        recommendations[row['Title']] += (row["UserTime"] * (row["Likes"] + row["Shares"] - row["Dislikes"])) + row["Comments"] + row["ViewCount"]
    
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    top_recommendations = [video[0] for video in sorted_recommendations[:3]]
    
    # add the recommended videos to the dict
    recommended_videos[user] = top_recommendations

    # print the recommended videos
    print(f"Recommended videos for {user}: {top_recommendations}")

# calculate engagement time for recommended videos
for user in users:
    user_df = df[df['User'] == user]
    for idx, row in user_df.iterrows():
        if row['Title'] in recommended_videos[user]:
            engagement_time[user] += row['UserTime'] * row['NumberOfTimesWatched']

# create the bar plot
users = list(engagement_time.keys())
total_engagement_times = list(engagement_time.values())

plt.bar(users, total_engagement_times)
plt.xlabel('User')
plt.ylabel('Total Engagement Time')
plt.title('User vs Total Engagement Time for Recommended Videos')

plt.show()
