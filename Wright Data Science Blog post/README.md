# Data Science Blog Post

### Table of Contents
- Introduction
- Data Wrangling
- Exploratory Data Analysis
- Conclusions
- 
## Introduction

I selected the soccer database from Kaggle. It contains more than 25,000 matches and more than 10,000 players ,
 players and from several European countries from 2008 to 2016. By means of Exploratory Data Analysis method. 
Although we won’t be getting into the details of it for our example, the dataset even has attributes on weekly
 game updates, team line up, and detailed match events. The goal of this notebook is to walk you through an end
 to end process of analyzing a dataset . Our simple analytical process will include some steps for exploring 
and cleaning our dataset.

### Research Questions

- we can predict the the winner of match based on this dataset
- we have the history of teams matches and thier players?
- can we identify the team or player belong to the best teams/players ?

## Research Question 1
at the end when megre all tables there will be cells have nulls ?

yes ,due to different shapes of tables

## Research Question 2
when merged ,it will affect in prediction ?

I think it is ,and we should select algorithm to work well with that dataset

## Research Question 3
is there a correlation betwween features ?
- there is positive correlation betwwen attack features and negative between attack and defense features .

I think it is ,and we should select algorithm to work well with that dataset

## Conclusions
Analyzing the league, country, player, player attributes, team, team atributes nad match tables gave a better understanding of the data. once features are meerged pass it to machine learning algorithm to predict the winner of the future match.

We use player attributes table to groups/cluster the players based on its skills like "passing","long pass" etc,to identify which player belong to this group.

And we can use any table and make our predction on it ,I selected the player attributes to make my own

## Medium link
https://am2958.medium.com/soccer-data-analysis-e911eccc8369
