#!/usr/bin/env python3
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import numpy as np
nltk.download('punkt')
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_rows', None)
"""
data loading function
"""


def load_data():
    data = pd.read_csv('b.csv', header=None)
    data.columns = ["datetime", "tweets", "user", "location"]
    return data

tweet_df = load_data()
tweet_df["originaltweets"] = tweet_df["tweets"]  # duplicating original tweets
tweet_df = tweet_df.dropna()  # removing rows containing null values
tweet_df = tweet_df.drop_duplicates()  # removing duplicates
tweet_df.reset_index(inplace=True)  # resetting index after removing duplicates

# data cleaning
# lowercasing all the letters
tweet_df['tweets'] = tweet_df['tweets'].str.lower()
# removing url
tweet_df['tweets'] = tweet_df['tweets'].str.replace(
    r'https?://[^ ]+', '', regex=True)
tweet_df['tweets'] = tweet_df['tweets'].str.replace(
    r'@[^ ]+', '', regex=True)  # removing mentions
# removing a pattern in the file
E = r'\\[a-zA-Z0-9-]+\\[a-zA-Z0-9]+\\[a-zA-Z0-9]+'
tweet_df['tweets'] = tweet_df['tweets'].str.replace(E, '', regex=True)
tweet_df['tweets'] = tweet_df['tweets'].str.replace(
    r'b\'', '', regex=True)  # removing a pattern
tweet_df['tweets'] = tweet_df['tweets'].str.replace(
    r'#', '', regex=True)  # hashtag removal
# removing all the punctuations
tweet_df['tweets'] = tweet_df['tweets'].str.replace(r'[^\w\s]', '', regex=True)
tweet_df['tweets'] = tweet_df['tweets'].apply(word_tokenize)  # tokenzing

# adding required columns for calculations
tweet_df["profanity"] = np.nan
tweet_df["totalwords"] = np.nan
tweet_df["degreeofprofanity"] = np.nan

a = ["racial", "slur", "white"]  # profain words assumed

length = len(tweet_df)  # length of dataframe for further use

"""
for loop to find out total words in a tweet and also counting the number of profain words in a tweet
"""

for i in range(0, length):
    b = 0
    c = len(tweet_df.loc[i][2])
    tweet_df.loc[tweet_df.index[i], 'totalwords'] = c
    for word in a:
        j = tweet_df.loc[i][2].count(word)
        b += j
    tweet_df.loc[tweet_df.index[i], 'profanity'] = b

"""
calculating degree of profanity
"""
for i in range(0, length):
    tweet_df.loc[tweet_df.index[i], 'degreeofprofanity'] = (
        tweet_df.loc[i][6]/tweet_df.loc[i][7])*100

# sorting the dataframe according to degree of profanity column with most profain tweet on top

print(tweet_df.sort_values(by='degreeofprofanity', ascending=False))
