# Email_Spam_Classifier
This is a project that was done for the Skill4U machine Learning program. This project is a Spam email classifier using machine learning. This model uses Gaussian NB algorithm to train the model.

## Problem Statement 
Spamming is one of the major and common attacks that accumulate a large number of compromised machines by sending unwanted messages, viruses, and phishing through email. We have chosen this project because now there are many people who are trying to fool you just by sending you fake e-mails

In recent figures, 40% of all mail is spam that emails about 15.4 billion emails per day and costs Internet users about $ 355 million per year. Automatic e-mail filtering is the most effective way to deal with spam at the moment

## Proposed Solution
The proposed solution for this problem is to use  Gaussian Naïve Bayes classifier, we have two classes to classify in either spam or ham emails. GaussianNB assumes that the data from each label is drawn from a simple Gaussian distribution. The Scikit-learn Library helps us to implement the Gaussian Naïve Bayes algorithm for classification.

## Execution Plan
We have proposed the following technique in order to classify emails
![image](https://user-images.githubusercontent.com/47780362/194686725-ec60e1da-4c81-47a1-bcf5-e7566361360d.png)

## Dataset
The Dataset used to train our model was taken from Kaggle. [https://www.kaggle.com/datasets/nitishabharathi/email-spam-dataset](https://www.kaggle.com/datasets/nitishabharathi/email-spam-dataset)
- This dataset contains 3 csv files each file contains 2 columns. 
- The first column is the body of the email
- The second column contains our labels 0 for Not Spam 1 for Spam
- Total values of the dataset of all 3 files is 18650

## How the data was cleaned
We cleaned the data using NLTK library for python and vanilla python functions. 
- We balanced our dataset
- Combined our 3 csv files into 1 dataset
- Removed links from the dataset body column
- Removed unnecessary symbols from our body column
- Changed all the text into lower case
- Performed word Tokenization
- Used Lemmatization to remove different forms of the same words
- Removed Stop words from our data
- Vectorized our data By bag of words method

## Algorithm
Algorithm comparison graph          |  Details
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/47780362/194687049-92bc68d1-4f81-425d-a973-7dff81ab3700.png)| We are using Gaussian NB algorithm for classification. We tested out different classification algorithms and GaussianNB was giving the best results on the test data

## Metrics

ROC Curve        |  Model Evaluation
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/47780362/194687025-9317a81d-68fb-4494-bb41-1c233ce2188a.png)  | After training and finding the best parameters we were able to get `90.07 %`  accuracy on our Test data

Confusion Matrix        |  Classification Report
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/47780362/194687186-6a4dcf41-6d17-4257-a65b-a015895ae31c.png)| ![image](https://user-images.githubusercontent.com/47780362/194687113-fbe78281-4ae0-45e2-8834-36e43ed9d5b8.png) 

## Target Audience
About 14.5 billion spam email messages are circulated daily. That is almost 45 percent of the regular email traffic in the world. Internet Service Providers (ISPs) use spam filters to ensure they do not deliver corrupt incoming emails or links to the receiver.

## Demonstration
On the left you can see how this model works. You can also try it out by scanning the QR code down below

Demo          |  Scan to see yourself
:-------------------------:|:-------------------------:
![demo](https://user-images.githubusercontent.com/47780362/194687277-05b0568b-dc75-411f-837c-c63d6fce3289.gif) | ![image](https://user-images.githubusercontent.com/47780362/194687249-0172a555-45c1-46d8-9ee2-cf072f54b111.png)

## Advantages
No more Spam         |  Benefits
:-------------------------:|:-------------------------:
![Spare_a_thought_for_your_Email_Spam_Filter](https://user-images.githubusercontent.com/47780362/194687406-58b11470-d757-479d-ba2f-230d56202b35.gif)|- It is very effective and is also adaptive, so hard to fool. Based on text classification methods. Phenomenally accurate. Learns new spammer tactics automatically. Adapt to changing spam. It protects you
