import ast
import os
import numpy as np
import pandas as pd

def convert(obj):
    L = []
    for i in ast.literal_eval():
        L.append(i['name'])
    return L

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000, stop_words="english")
vectors=cv.fit_transform(new_df["tag"]).toarray()
cv.get_feature_names()

import nltk
from nltk.stem.porter import PorterStemmer
ps= PorterStemmer()
def stem (text):
    for i in text.split():
        ps.stem(i)