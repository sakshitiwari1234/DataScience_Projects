# -*- coding: utf-8 -*-
"""Exploring 20 Newsgroup Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X0g3tgUmUX6NIqD7W1UBHplJD68NXN1a

### We shall perform  the following steps to explore the dataset

What is nlp?
touring python nlp libraries
NTLK
the newsgroup data
getting the data
thinking about features
visualizing the data
data preorocessing
clustering and unseupervised learning
k means clustering
non negatvie matrix factorization
toopic modelling

#### the way we represent and roganize  the task and concepts is called as ontology.
"""

import nltk

nltk.download()

from nltk.corpus import names
nltk.download('names')

print( names.words() [:10])

print (len(names.words()))

"""Importing the stemmer and lemmitizer techniques"""

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

# Stem machines learning :

porter_stemmer.stem('machines')
porter_stemmer.stem('learn')

"""Stemming sometimes , chop off the letters , as it happened in machine it only printed machin"""

porter_stemmer.stem('machines')

"""Now , i am importing the lemmitization algorithm based on wordnet corpus built in , and intilize lemmatizer.


"""

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

"""lemmatizing machine learning word.

"""

nltk.download('wordnet')

lemmatizer.lemmatize('machines')

lemmatizer.lemmatize('schooling')

"""there are two libraries  - Gensim and TextBlob which have more librariry function which is on top of NLTK. it simplfies nlp and text analysis , which have easy to use built in functions.

we can install textblob just by using  -> pip install -U textblob

### The NewsGroup Data.

This project comprises of 20 newsgroup dataset , which is available Sci-kit learn. The data contains approxiamtely 20,000 across 20 online newsgroup.

A newsgroup is an place on internet where you can ask and answer questions about certain topic.

The data is already split into train and test sets.
"""

from sklearn.datasets import fetch_20newsgroups

groups = fetch_20newsgroups()



groups.data[0]

import seaborn as sns

sns.distplot(groups.target)

"""we are using word counts in this as features , as each feature is highly dimesnional.
For count of words having only one unigram kind of words that is only one root word , we will use countvecotrizer in that.
"""

from sklearn.feature_extraction.text import CountVectorizer

import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from nltk.corpus import names
from nltk.stem import WordNetLemmatizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def letters_only(astr):
     return astr.isalpha()

cv = CountVectorizer(stop_words = "english", max_features = 500)
groups = fetch_20newsgroups()
cleaned = []
all_names = set(names.words())
lemmatizer = WordNetLemmatizer()


for post in groups.data:
   cleaned.append(' '.join([lemmatizer.lemmatize(word.lower())
                                for word in post.split()
                                if letters_only(word)
                                and word not in all_names ]))


transformed = cv.fit_transform(cleaned)
km = KMeans(n_clusters = 20)
km.fit(transformed)
labels = groups.target
plt.scatter(labels, km.labels_)
plt.xlabel("newsgroups")
plt.ylabel("cluster")
plt.show()

"""### Topic Modelling

we are performing NMF ( nON NEGATIVE MATRIX factorization)
it facotrizes a matrix into the form of product of two smaller matrices.
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from nltk.corpus import names
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import NMF
def letters_only(astr):
  return astr.isalpha()

cv = CountVectorizer(stop_words="english", max_features=500)
groups = fetch_20newsgroups()
cleaned = []

all_names = set(names.words())
lemmatizer = WordNetLemmatizer()
# for post in groups.data:
#   cleaned.append(' '.join([lemmatizer
#                            .lemmatize(words.lower())
#                            if letters_only(word)
#                            and word_not in all_names]))


for post in groups.data:
   cleaned.append(' '.join([lemmatizer.lemmatize(word.lower())
                                for word in post.split()
                                if letters_only(word)
                                and word not in all_names ]))

transformed = cv.fit_transform(cleaned)
nmf = NMF(n_components=100, random_state = 43).fit(transformed)
for topic_idx , topic in enumerate(nmf.components_):
  label = '{}  '.format(topic_idx)
  print(label, " ".join([cv.get_feature_names_out()[i]
                         for i in topic.argsort() [:-9: -1]]))

