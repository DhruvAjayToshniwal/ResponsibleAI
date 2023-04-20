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
1) Data Generation Script
The data generation script is responsible for creating synthetic datasets representing user behavior on a video-sharing platform. The datasets contain information about the videos watched by multiple users, including video title, uploader, and hours watched.

The script generates five separate CSV files, each with 15,000 rows. Each row represents a video watched by a user. The datasets include a mix of normal videos (e.g., chess, music, or gaming) and challenge videos, with a special focus on the "Condom Challenge" to align with the case study.

2) Recommendation System
The optimized recommendation system is designed to provide personalized video recommendations based on user behavior while minimizing memory usage. It uses a hybrid approach that combines item-based collaborative filtering with content-based filtering using video titles.

The recommendation system processes each CSV file separately to reduce the memory footprint. For each user, it calculates the cosine similarity between video titles in the dataset. The cosine similarity is a measure of similarity between two vectors, in this case, the TF-IDF (term frequency-inverse document frequency) vectors of the video titles. The higher the cosine similarity, the more related the two video titles are.

The system accumulates similarity scores for each recommended video and returns the top 3 recommendations with the highest accumulated scores. This approach leverages the information about the videos watched by a user to provide personalized recommendations.

## Auditing Plan

The auditing plan will be developed at a later stage of the project, considering the following aspects:

- Audit objectives
- Auditors
- What is being audited and when
- Methods, tools, metrics, and standards
