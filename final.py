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




