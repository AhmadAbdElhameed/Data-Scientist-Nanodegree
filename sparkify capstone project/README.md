# Sparkify-Capstone-Project
## Task : Determine customer churn for a music streaming for Sparkify company.

## Table of Contents
- Installation
- Project Motivation
- File Descriptions
- Results
- Licensing, Authors, and Acknowledgements
## Installation
**This project uses the following software and python libraries**

- Python 3.6
- Pyspark-2.4.1
- NumPy
- Pandas
- scikit-learn
- matplotlib
- Jupyter Notebook

Project Motivation
Imagine you are working for music streaming company like Spotify or Pandora called Sparkify.Millions of users stream thier favorite songs everyday. Each user uses either the Free-tier with advertisement between the songs or the premium Subscription Plan.Users can upgrade, downgrade or cancel thier service at any time.Hence, it's crucial to make sure that users love the service provided by Sparkify. Every time a users interacts with the Sparkify app data is generated. Events such as playing a song, logging out, like a song etc. are all recorded. All this data contains key insights that can help the business thrive. The goal of this project is then to analyse this data and predict which group of users are expected to churn - either downgrading from premium to free or cancel thier subscriptions altogether.

In this project we'll be performing the following tasks:

Data Exploration
Learn about the data
Define Churn and label data based on churn definition
Determine which feature or feature value can be user to defin churn
Feature Engineering
Create features for each user. This data will be used as input to the model
Data transformation, data splitting and model training
Transform feature engineered data.
Split data into training, validation and test data.
Build a machine learning model to train using training data
File Descriptions
Sparkify-Capstone-Project : Jputer notebook used for this project
main_sparkify.py: python script extracted from the notebook
Results
We have analysed the sparkify dataset and come up with new features to predict churn. We then created a machine learning model and tuned it to improve its performance. We achieved an accuracy score of - and F1 score of - on the test dataset.

Conclusion
We are able to achieve an accuracy score of 87% and F1 score of 84% on the test dataset using the tuned Random Forest algorithm. The model peformance can be further improved by creating additional features and includiding some of the features that I have left out for this analysis. The model should also be tested using samples from the left out big dataset which hasn't been used for this analysis. Once we are satified with the result, a large scale of the model can be implemented on the cloud.
