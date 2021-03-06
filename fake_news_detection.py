# -*- coding: utf-8 -*-
"""Fake_News_Detection

Automatically generated by Colaboratory.
"""

#Desciption: This program detects real and fake news

#Import the libraries
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string

#Load the data
from google.colab import files
files.upload()

df = pd.read_csv('fake_or_real_news.csv')
df.head()

df.shape

# Check and delete duplicates
df.drop_duplicates(inplace=True)
df.shape

df.isnull().sum()

# Remove null data
df.dropna(axis=0, inplace=True)
df.shape

#Download the stopwords
nltk.download('stopwords')

#Process the text
def process_text(txt):
  #Remove the punctuation
  no_punc = [char for char in txt if char not in string.punctuation]
  no_punc = ''.join(no_punc)
  #Remove the stopwords
  clean_words = [word for word in no_punc.split() if word.lower() not in stopwords.words('english')]
  return clean_words

#Filter the texts
from sklearn.feature_extraction.text import CountVectorizer
message_bow = CountVectorizer(analyzer=process_text).fit_transform(df['title'])

#Parse the datas
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(message_bow, df['label'], test_size=0.2, random_state=0)

message_bow.shape

#Create the model
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
classifier.fit(x_train, y_train)

print(classifier.predict(x_train))
print(y_train.values)

#Accuracy on the train data
from sklearn.metrics import classification_report
pred = classifier.predict(x_train)
print(classification_report(y_train, pred))

#Accuracy on the test data
pred = classifier.predict(x_test)
print(classification_report(y_test, pred))
