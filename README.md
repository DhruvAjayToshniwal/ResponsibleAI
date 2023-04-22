# ResponsibleAI
# Feedback Loop and Amplification in Recommendation Systems

This project explores the effects of feedback loop and amplification in recommendation systems, specifically for dangerous and harmful content on YouTube and TikTok.

## Table of Contents

1. [Project Concept](#project-concept)
2. [Motivation & Context](#motivation--context)
3. [System Definitions](#system-definitions)
4. [Deployment of the System](#deployment-of-the-system)
5. [Integration in the Organization Processes](#integration-in-the-organization-processes)
6. [Case Study](#case-study)
7. [Code](#code)
8. [Auditing Plan](#auditing-plan)

## Project Concept

The project aims to understand the feedback loop and amplification in recommendation systems, specifically on platforms like YouTube and TikTok, that may lead to the promotion of dangerous and harmful content.

## Motivation & Context

The problem of feedback loop and amplification in recommendation systems is important to solve because it can result in:

- Missing diversity
- Echo-chamber effects
- Privacy concerns

Stakeholders related to this problem and its solution include:

- Consumers/users
- Investors
- Business holders
- National interest/government

## System Definitions

The system's outputs are content recommendations (photos/videos) that viewers might enjoy.

The specific decisions the system takes include:

- Identifying user interests
- Generating recommendations
- Filtering recommendations
- Personalizing user experiences
- Promoting engagement

The system accepts inputs like viewer interests (likes, shares, comments, time spent on app/video/post), and it requires data for storing user interests and training the recommendation system.

Data is collected by tracking user actions, and while it is not tagged, self-supervision is utilized.

## Deployment of the System

The deployment of the system will be detailed in a later stage of the project.

## Integration in the Organization Processes

The integration of the system in the overall activity of the organization is not relevant at this stage of the project.

## Case Study

A 14-year-old girl from Napoli (Italy) was suffocated due to an allergic reaction to latex. Her mom found her in her room, unable to breathe, holding a wet condom. After rushing her to the ER, the mom scrolled through her daughter’s TikTok and YouTube apps to try and figure out what she was doing with a condom. She was shocked to see several videos of older teenagers attempting “The Condom Snorting Challenge”, in which one has to snort a condom through the nostril, then spit it out from the mouth. After the daughter’s condition was stabilized, the mom questioned her about the videos. The daughter was surprised, stating “I didn’t look for these, they just kept showing up. There are so many of them, it seems like everyone is doing this. Cosa c’è di strano, mamma?”

## Code

The code for this project can be found in this repository.

Explanation 
1) Data Generation Script:
This is a Python script that generates a synthetic dataset of user video-watching behavior. The script creates a total of 75,000 rows of data across 5 different CSV files (15,000 rows per file) using the pandas library.

The dataset consists of the following columns:

User: the user who watched the video
Title: the title of the video
Duration: the duration of the video in minutes
ViewCount: the number of views the video has
UserTime: the total amount of time the user spent watching the video, in minutes
NumberOfTimesWatched: the number of times the user watched the video
Likes: the number of likes the video received
Dislikes: the number of dislikes the video received
Shares: the number of times the video was shared
Comments: the number of comments the video received
The video titles are generated randomly based on a set of predefined video types, challenges, and uploaders. Certain users (in this case, the user "Giulia") have a higher likelihood of watching videos of a certain type, and may also be recommended certain videos based on their past viewing behavior.

This dataset could be used for various purposes, such as building a recommendation system or analyzing patterns in user video-watching behavior.

2) Recommendation System:
This code snippet uses a recommendation system to suggest top 3 videos for a list of users based on their video-watching history. The dataset is generated using random sampling and consists of information about users, video titles, duration, view count, user time, number of times watched, likes, dislikes, shares, and comments.

The code reads in the dataset, creates a TF-IDF vector for the video titles, and calculates cosine similarity between the vectors to obtain a similarity matrix. It then uses the similarity matrix to find the most similar videos to those watched by a specific user. These similar videos are then assigned an engagement score based on their user time, likes, dislikes, shares, and number of times watched. The scores are aggregated to create a list of recommendations for each user.

The output of the code is a list of top 3 video recommendations for each user. These recommendations are generated using data from five different datasets to increase the size of the dataset and improve the accuracy of the recommendations.

## Auditing Plan

The auditing plan will be developed at a later stage of the project, considering the following aspects:

- Audit objectives
- Auditors
- What is being audited and when
- Methods, tools, metrics, and standards
