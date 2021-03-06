
# Importing packages

import os
import pandas as pd
import re
import string
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Setting working directory

os.chdir(r'/Users/lucaspb/git-repositories/portifolio-projects')

#############################
#                           #
#     Cleaning the Text     #
#                           #
#############################

#Reading a File as a big string

## with open('NLP/data/rochel.txt', 'r', encoding='utf-8') as df:
##   data = df.read()
##     data = "".join(data.splitlines())
##     data = data.replace("\t", " ")
##   text 
  
#Reading a File as small strings

text = open ("nlp-learning/input/rochel.txt", "r", encoding='utf-8')
print(text.read())
text.seek(0)

#Transforming in Data Frame

pd.set_option('max_colwidth',150)

data = pd.DataFrame(text)

print(data.head(5))
data.columns

## Changing the column name
data.columns = ['transcript']

### data = ' '.join(data.transcript)

# Let's pickle it for later use
data.to_pickle("nlp-learning/output/corpus/corpus.pkl")


#############################
#                           #
#     Cleaning the Text     #
#                           #
#############################


# Apply a first round of text cleaning techniques

def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

round1 = lambda x: clean_text_round1(x)

# Let's take a look at the updated text
data_clean = pd.DataFrame(data.transcript.apply(round1))
data_clean

# Apply a second round of cleaning
def clean_text_round2(text):
    '''Get rid of some additional punctuation and non-sensical text that was missed the first time around.'''
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    return text

round2 = lambda x: clean_text_round2(x)

# Let's take a look at the updated text
data_clean = pd.DataFrame(data_clean.transcript.apply(round2))
data_clean



#############################
#                           #
#   Document-Term Matrix    #
#                           #
#############################

# We are going to create a document-term matrix using CountVectorizer, and exclude common English stop words
## pip install sklearn.feature_extraction.text

cv = CountVectorizer(stop_words='english')
data_cv = cv.fit_transform(data_clean.transcript)
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_dtm.index = data_clean.index


# Transposing and joining data counted
data_dtm = data_dtm.transpose()
data_dtm['total']= data_dtm.sum(axis=1)
data_dtm.drop(data_dtm.columns.difference(['total']), 1, inplace=True)
print (data_dtm.head(5))
data_dtm.columns = ['Rochel']
data_dtm = data_dtm.transpose()

# Let's pickle it for later use
data_dtm.to_pickle("nlp-learning/output/corpus/dtm.pkl")

# Let's also pickle the cleaned data (before we put it in document-term matrix format) and the CountVectorizer object
data_clean.to_pickle('nlp-learning/output/corpus/data_clean.pkl')
pickle.dump(cv, open("nlp-learning/output/corpus/cv.pkl", "wb"))



