import matplotlib.pyplot as plt

fig, axes = plt.subplots(3, 2, figsize=(15, 15))


# # Plot Unique Video Types Over Time
for user, unique_video_types in dangerous_recommended.items():
    axes[0, 0].plot(unique_video_types, label=user)
axes[0, 0].set_title('Dangerous Recommended Videos Over Time')
axes[0, 0].set_xlabel('Day')
axes[0, 0].set_ylabel('Dangerous Recommended Videos')
axes[0, 0].legend()

# # Plot Unique Video Types Over Time
for user, unique_video_types in dangerous_watched.items():
    axes[0, 1].plot(unique_video_types, label=user)
axes[0, 1].set_title('Dangerous Watched Videos Over Time')
axes[0, 1].set_xlabel('Day')
axes[0, 1].set_ylabel('Dangerous Recommended Watched')
axes[0, 1].legend()


# Plot Mean Video Recommendation Variance Over Time
axes[1, 0].plot(all_var)
axes[1, 0].set_title("Mean Video Recommendation Variance Over Time")
axes[1, 0].set_xlabel('Day')
axes[1, 0].set_ylabel('Mean Recommendation Varience')


# # Plot Unique Video Types Over Time
for user, unique_video_types in unique_video_types_over_time.items():
    axes[1, 1].plot(unique_video_types, label=user)
axes[1, 1].set_title('Unique Video Types Over Time')
axes[1, 1].set_xlabel('Day')
axes[1, 1].set_ylabel('Unique Video Types')
axes[1, 1].legend()

# Graph 1: Progress from day 1 to day 5 for Giulia and Christopher
giulia_progress = []
christopher_progress = []

for i in range(1, 10):
    chunk=chunks[i]
    giulia_chunk = chunk[chunk["User"] == "Giulia"]
    christopher_chunk = chunk[chunk["User"] == "Christopher"]

    giulia_watched = giulia_chunk["NumberOfTimesWatched"].sum()
    christopher_watched = christopher_chunk["NumberOfTimesWatched"].sum()

    giulia_progress.append(giulia_watched)
    christopher_progress.append(christopher_watched)




# Graph 2: Dangerous videos watched by all users
dangerous_videos = ["Condom Challenge"]
users_dangerous_videos = defaultdict(int)

for user in users:
    user_chunk = chunk[chunk["User"] == user]
    for video_title in dangerous_videos:
        user_dangerous_videos = user_chunk[user_chunk["Title"].str.contains(video_title)]
        users_dangerous_videos[user] += user_dangerous_videos["NumberOfTimesWatched"].sum()

axes[2, 1].bar(users_dangerous_videos.keys(), users_dangerous_videos.values())
axes[2, 1].set_xlabel('User')
axes[2, 1].set_ylabel('Dangerous Videos Watched')
axes[2, 1].set_title('Dangerous Videos Watched by All Users on the last day')

for user in users:
    user_chunk = recommendation[10][recommendation[10]["User"] == user]
    for video_title in dangerous_videos:
        user_dangerous_videos = user_chunk[user_chunk["Title"].str.contains(video_title)]
        users_dangerous_videos[user] += user_dangerous_videos["NumberOfTimesWatched"].sum()

axes[2, 0].bar(users_dangerous_videos.keys(), users_dangerous_videos.values())
axes[2, 0].set_xlabel('User')
axes[2, 0].set_ylabel('Dangerous Videos Recommended')
axes[2, 0].set_title('Dangerous Videos Recommended for All Users after the last day')

# Adjust the layout of the subplots and display the plots
plt.tight_layout()
plt.show()
