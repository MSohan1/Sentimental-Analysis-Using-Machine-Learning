# -*- coding: utf-8 -*-
"""Sentiment Analysis .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1018abPEbl4T_yz84BZqyw-8UkIDmhmXu
"""

import pandas as pd 
import numpy as np



df= f=pd.read_table('/content/reviewsnew (1) (1).txt',encoding='utf-8')
df

# library to clean data
import re

# Natural Language Tool Kit
import nltk

nltk.download('stopwords')

# to remove stopword
from nltk.corpus import stopwords

# for Stemming propose
from nltk.stem.porter import PorterStemmer

# Initialize empty array
# to append clean text
corpus = []

# 1000 (reviews) rows to clean
for i in range(0, 1500):
	
	# column : "Review", row ith
	review = re.sub('[^a-zA-Z]', ' ', df['Review'][i])
	
	# convert all cases to lower cases
	review = review.lower()
	
	# split to array(default delimiter is " ")
	review = review.split()
	
	# creating PorterStemmer object to
	# take main stem of each word
	ps = PorterStemmer()
	
	# loop for stemming each word
	# in string array at ith row
	review = [ps.stem(word) for word in review
				if not word in set(stopwords.words('english'))]
				
	# rejoin all string array elements
	# to create back into a string
	review = ' '.join(review)
	
	# append each string to create
	# array of clean text
	corpus.append(review)
corpus

df['Review']

df['Liked'].value_counts()

import seaborn as sns
sns.distplot(df['Liked'])

x = df['Review'].values
y = df['Liked'].values

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0)

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(stop_words ='english')
x_train_vect= vect.fit_transform(x_train)
x_test_vect= vect.transform(x_test)

"""**using support vector machines**"""

from sklearn.svm import SVC
model1 = SVC()

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(stop_words ='english')
x_train_vect= vect.fit_transform(x_train)
x_test_vect= vect.transform(x_test)

model1.fit(x_train_vect,y_train)

y_pred1 = model1.predict(x_test_vect)
y_pred1

y_test

y_pred1 = model1.predict(x_test_vect)
y_pred1

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_pred1,y_test)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred1)

print(cm)

# Accuracy, Precision and Recall
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
score1 = accuracy_score(y_test,y_pred1)
score2 = precision_score(y_test,y_pred1,pos_label='positive',average='micro')
score3= recall_score(y_test,y_pred1,pos_label='positive',average='micro')
print("\n")
print("Accuracy is ",round(score1*100,2),"%")
print("Precision is ",round(score2,2))
print("Recall is ",round(score3,2))

"""### sklearn pipeline (countvector+svc)"""

from sklearn.pipeline import make_pipeline
model2 = make_pipeline(CountVectorizer(),SVC())
model2.fit(x_train,y_train)
y_pred2 = model2.predict(x_test)
y_pred2

from sklearn.metrics import accuracy_score
accuracy_score(y_pred2,y_test)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred2)

print(cm)

# Accuracy, Precision and Recall
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
score1 = accuracy_score(y_test,y_pred2)
score2 = precision_score(y_test,y_pred2,pos_label='positive',average='micro')
score3= recall_score(y_test,y_pred2,pos_label='positive',average='micro')
print("\n")
print("Accuracy is ",round(score1*100,2),"%")
print("Precision is ",round(score2,2))
print("Recall is ",round(score3,2))

"""**naive** **bayes**"""

from sklearn.naive_bayes import MultinomialNB
model3 = MultinomialNB()

model3.fit(x_train_vect,y_train)

y_pred3 = model3.predict(x_test_vect)
y_pred3

from sklearn.metrics import accuracy_score
accuracy_score(y_pred3,y_test)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred3)

print(cm)

# Accuracy, Precision and Recall
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
score1 = accuracy_score(y_test,y_pred3)
score2 = precision_score(y_test,y_pred3,pos_label='positive',average='micro')
score3= recall_score(y_test,y_pred3,pos_label='positive',average='micro')
print("\n")
print("Accuracy is ",round(score1*100,2),"%")
print("Precision is ",round(score2,2))
print("Recall is ",round(score3,2))

"""sklearn pipeline (countvetorizer+nb)"""

from sklearn.pipeline import make_pipeline
model4 = make_pipeline(CountVectorizer(),MultinomialNB())
model4.fit(x_train,y_train)
y_pred4 = model4.predict(x_test)
y_pred4

from sklearn.metrics import accuracy_score
accuracy_score(y_pred4,y_test)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred4)

print(cm)

# Accuracy, Precision and Recall
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
score1 = accuracy_score(y_test,y_pred4)
score2 = precision_score(y_test,y_pred4,pos_label='positive',average='micro')
score3= recall_score(y_test,y_pred4,pos_label='positive',average='micro')
print("\n")
print("Accuracy is ",round(score1*100,2),"%")
print("Precision is ",round(score2,2))
print("Recall is ",round(score3,2))

import joblib
joblib.dump(model2,'positive-negative')

reloaded_model =joblib.load('positive-negative')
reloaded_model

pip install streamlit==1.13.0

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import joblib
# st.title("SENTIMENTAL ANALYSIS")
# reloaded_model = joblib.load('positive-negative')
# input1 = st.text_input("Enter the Review")
# output1=reloaded_model.predict([input1])
# if st.button("PRIDTICTE"):
#   op=['Neutral','Positive','Negative']
#   st.title(op[output1[0]])

!streamlit run app.py & npx localtunnel --port 8501

"""**sentimental** **analysis**

Sentiment analysis is use to detect the human emotion through text.It is a natural language processing which use to detect either positive,negative and neutral statement in the text.
It is mostly used by the new organisations to know the openion of the coustomer about the product,which help the growth of the company
Sentiment analysis predict the emotion(positive,negative,neutral) based on the polarity of the text.Itcan dectect beyond the polarity value for finding the emotions like anger,said,happy and the intention like intrested or not intersted.

**Twitter** **sentiment**

Twitter sentiment analysis are continously changes,ther are some hashtags and emoji are also need to be analysis for predicting more accuratly about the perticular twitte.
 for example consider a stock market analysis by analysing the twitte and predecting the increasing or decreasing the strock for that we can use regration algorithem to predict the continous data .
"""