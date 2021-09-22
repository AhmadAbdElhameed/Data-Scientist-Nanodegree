# Sparkify-Capstone-Project
## Task : Determine customer churn for a music streaming for Sparkify company.

## Table of Contents
- Installation
- Project Motivation
- Results
- Conclusion
## Installation
**This project uses the following software and python libraries**

- Python 3.6
- Pyspark-2.4.1
- NumPy
- Pandas
- scikit-learn
- matplotlib
- Jupyter Notebook

## Project Motivation
Imagine you are working for music streaming company like Spotify or Pandora called Sparkify.
Millions of users stream thier favorite songs everyday. 
Each user uses either the Free-tier with advertisement between the songs or the premium Subscription Plan.
Users can upgrade, downgrade or cancel thier service at any time.Hence, it's crucial to make sure that users love the service provided by Sparkify. 
Every time a users interacts with the Sparkify app data is generated. 
Events such as playing a song, logging out, like a song etc. are all recorded. 
All this data contains key insights that can help the business thrive. 
The goal of this project is then to analyse this data and predict which group of users are expected to churn - either downgrading from premium to free or cancel thier subscriptions altogether.

## Project Definition
### Project Overview
Sparkify Capstone Project is Udacity’s Data Science final project it explores the user churn rate for Sparkify company. Dataset provided with the 128MB of activity log for a number of users and the different activities that can be done via the (web) app.
### Problem Statement
the problem is to find some features that correlate whether a user will churn or not.
Definition of Churn: The user completing the cancellation process and reaching the “Cancellation Completed” page.
What I will do in this project
1. Load the dataset
2. Clean up any null and space values
3. Explore the dataset and learn some basic insights about it
4. create a new dataset containing only the features we want
5. Engineer new features to help me to improve prediction
6. compare between 5 algorithms to find the best one

## Metrics
I will use accuracy score
**Accuracy Score: a metric that anyone can understand**

## Analysis
### Data Exploration and Questions
#### Dataset
Each row represents an activity that one user undertook at a particular time from a particular device. If the activity was listening to a song (most of them are), then we will see the artist and song they listened to. we have 278,154 rows over 24 columns.
The dataset contains log files that generate entries whenever a user makes an action on a site, like picking the next song, giving a song a ‘thumbs down, or landing onto a new page. These files take into account information about the user, such as their location, user agent string for accessing the site, and account level: free or paid. It’s important to note that those who use the free service receive advertisements. Let’s take a look at

root
 |-- artist: string (nullable = true)
 
 |-- auth: string (nullable = true)
 
 |-- firstName: string (nullable = true)
 
 |-- gender: string (nullable = true)
 
 |-- itemInSession: long (nullable = true)
 
 |-- lastName: string (nullable = true)
 
 |-- length: double (nullable = true)
 
 |-- level: string (nullable = true)
 
 |-- location: string (nullable = true)
 
 |-- method: string (nullable = true)
 
 |-- page: string (nullable = true)
 
 |-- registration: long (nullable = true)
 
 |-- sessionId: long (nullable = true)
 
 |-- song: string (nullable = true)
 
 |-- status: long (nullable = true)
 
 |-- ts: long (nullable = true)
 
 |-- userAgent: string (nullable = true)
 
 |-- userId: string (nullable = true)
 
 |-- event_time: string (nullable = true)
 
 |-- registration_time: string (nullable = true)
### Missing Data
In terms of null values present, we have two cases:
#### case 1: userId, userAgent, firstName , lastName, gender, location, registration
About 8,000 rows are sessions picked up before the user has logged in — all redundant data for our purposes and to be cleaned away.
#### case 2:artist, length, song
About 58,000 rows are nulls occur when the user adds friends or gives a song thumbs up, all useful for our purposes and definitely data to keep.
## Modeling:
I split the full dataset into train and test sets. Test out the baseline of four machine learning methods: Logistic Regression, Decision Tree Classifier, Naive Bayes, Random Forest Classifier, and GradientBoostedTreeClassifier.


## Results
I have analyzed the sparkify dataset and come up with new features to predict churn. The best performance models are random forest and gradient boosted tree
## Model Tuning and Improve Performance
I will use Random Forest Tree to perform cross-validation
there was a little bit increasing in accuracy .
## Conclusion
We are able to achieve an accuracy score of 60 % with random forest and 60 for Gradient Boosted Tree and after applied cross-validation, the accuracy increased by almost 3%
## Future Work
Feature Engineering and Modeling we used Spark and whilst it's greater to have a tool that can handle big data
it's great for large datasets where you can run out of memory, but very time-consuming when you are running through the processing steps every time.
There is potential to improve the model and add a lot more features from the activity log data provided.
## Blog Post
https://am2958.medium.com/sparkify-capstone-project-2b9eb2bc4a76
