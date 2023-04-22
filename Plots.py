# Video vs video engagement graph
video_engagement = chunk.groupby("Title")[["Likes", "Shares", "Comments", "Dislikes"]].sum()
video_engagement["Total Engagement"] = video_engagement["Likes"] + video_engagement["Shares"] + video_engagement["Comments"] - video_engagement["Dislikes"]
video_engagement[["Likes", "Shares", "Comments", "Dislikes"]].plot.bar(stacked=True, figsize=(15, 7), colormap='Pastel1', title="Video vs Video Engagement")
plt.xlabel("Video")
plt.ylabel("Engagement")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

# read in the dataset
df = pd.concat([pd.read_csv(f"dataset_{i}.csv") for i in range(1, 6)])

# create a dictionary of watched counts by user
watched_counts = defaultdict(int)
for _, row in df.iterrows():
    watched_counts[row['User']] += row['NumberOfTimesWatched']

# create the line plot
users = list(watched_counts.keys())
watched_times = list(watched_counts.values())

plt.plot(users, watched_times)
plt.xlabel('User')
plt.ylabel('Number of times video watched')
plt.title('User vs Number of times video watched')

# mark recommended videos for Giulia
giulia_recommended = ['Condom Challenge by Nelk Boys', 'Condom Challenge by Pewdiepie', 'Condom Challenge by Joe Rogan']
if 'Giulia' in users:
    giulia_index = users.index('Giulia')
    giulia_watched_times = watched_times[giulia_index]
    plt.plot(giulia_index, giulia_watched_times, 'ro')
    for i, video in enumerate(top_recommendations):
        if video in giulia_recommended:
            # get the video title from the dataset
            video_title = df.loc[df['Title'] == video, 'Title'].values[0]
            plt.annotate(f'Recommended {i+1}: {video_title}', xy=(giulia_index, giulia_watched_times), xytext=(giulia_index+0.1, giulia_watched_times+50), arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
