import matplotlib.pyplot as plt

fig, axes = plt.subplots(3, 2, figsize=(15, 15))

# Plot Engagement Score Over Time
for user, engagement_scores in engagement_score_over_time.items():
    axes[0, 0].plot(engagement_scores, label=user)
axes[0, 0].set_title('Engagement Score Over Time')
axes[0, 0].set_xlabel('Day')
axes[0, 0].set_ylabel('Engagement Score')
axes[0, 0].legend()

# Histogram of User Engagement
for user, user_engagements in user_engagement_over_time.items():
    axes[0, 1].hist(user_engagements, bins=5, alpha=0.5, label=user)
axes[0, 1].set_title('User Engagement Over Time')
axes[0, 1].set_xlabel('User Engagement')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].legend()

# Plot Total Video Views Over Time
axes[1, 0].plot(video_views_over_time['Total'], label='Total Views')
axes[1, 0].set_title('Total Video Views Over Time')
axes[1, 0].set_xlabel('Day')
axes[1, 0].set_ylabel('Total Video Views')
axes[1, 0].legend()

# Plot Unique Video Types Over Time
for user, unique_video_types in unique_video_types_over_time.items():
    axes[1, 1].plot(unique_video_types, label=user)
axes[1, 1].set_title('Unique Video Types Over Time')
axes[1, 1].set_xlabel('Day')
axes[1, 1].set_ylabel('Unique Video Types')
axes[1, 1].legend()

# Graph 1: Progress from day 1 to day 5 for Giulia and Christopher
giulia_progress = []
christopher_progress = []

for i in range(1, 6):
    chunk = pd.read_csv(f"dataset_{i}.csv")
    giulia_chunk = chunk[chunk["User"] == "Giulia"]
    christopher_chunk = chunk[chunk["User"] == "Christopher"]

    giulia_watched = giulia_chunk["NumberOfTimesWatched"].sum()
    christopher_watched = christopher_chunk["NumberOfTimesWatched"].sum()

    giulia_progress.append(giulia_watched)
    christopher_progress.append(christopher_watched)

axes[2, 0].plot(range(1, 6), giulia_progress, label='Giulia')
axes[2, 0].plot(range(1, 6), christopher_progress, label='Christopher')
axes[2, 0].set_xlabel('Day')
axes[2, 0].set_ylabel('Videos Watched')
axes[2, 0].set_title('Progress from Day 1 to Day 5')
axes[2, 0].legend()

# Graph 2: Dangerous videos watched by all users
dangerous_videos = ["Ice Bucket Challenge", "Cinnamon Challenge", "Condom Challenge", "Mannequin Challenge", "Hot Pepper Challenge", "Try Not to Laugh Challenge", "Whisper Challenge"]
users_dangerous_videos = defaultdict(int)

for user in users:
    user_chunk = chunk[chunk["User"] == user]
    for video_title in dangerous_videos:
        user_dangerous_videos = user_chunk[user_chunk["Title"].str.contains(video_title)]
        users_dangerous_videos[user] += user_dangerous_videos["NumberOfTimesWatched"].sum()

plt.bar(users_dangerous_videos.keys(), users_dangerous_videos.values())
plt.xlabel('User')
plt.ylabel('Dangerous Videos Watched')
plt.title('Dangerous Videos Watched by All Users')
plt.show()
