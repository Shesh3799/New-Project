import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('data.csv',usecols=["symptoms"])

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 471):
    symptoms = re.sub('[^a-zA-Z]', ' ', str(dataset['symptoms'][i]))
    symptoms = symptoms.lower()
    symptoms = symptoms.split()
    ps = PorterStemmer()
    symptoms = [ps.stem(word) for word in symptoms if not word in set(stopwords.words('english'))]
    symptoms = ' '.join(symptoms)
    corpus.append(symptoms)
x=set()
for i in corpus:
    y=i.split()
    for j in range(len(y)):
        x.add(y[j])
x=list(x)
x.sort()
print(x)
print(len(x))
