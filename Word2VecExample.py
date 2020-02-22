# Import Libraries
import pandas as pd
import numpy as np
import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
nltk.download('stopwords')

#Reading Dataset
data=pd.read_csv("IMDB_Dataset.csv")
#print(data.head())

#create empty list
review_data_list = list()

#Adding reviews in list
reviews = data['review'].values.tolist()

for line in reviews:
	#create word tokens as well as remove puntuation in one go
	rem_tok_punc = RegexpTokenizer(r'\w+')   # '\w+' ===> '[a-zA-Z0-9]+'
	tokens = rem_tok_punc.tokenize(line)

#convert the words to lower case
	words = [w.lower() for w in tokens]

#Invoke all the english stopwords
	stop_word_list = set(stopwords.words('english'))

#Remove stop words
	words = [w for w in words if not w in stop_word_list]

#Append words in the review_data_list list.
	review_data_list.append(words)
print(len(review_data_list))

#Train a Word2Vec model using Gensim
import gensim
Embedding_Dim = 100
#train word2vec model
model = gensim.models.Word2Vec(sentences = review_data_list, size = Embedding_Dim, workers = 4, min_count = 1)

#Vocabulary size
words = list(model.wv.vocab)
print('Here is the Vocabulary Size.. %d' % len(words))

#Fining similar words like 'Amazing' and 'Awful'
print(model.wv.most_similar('amazing'))
print(model.wv.most_similar('awful'))

#Performing some mathematics on word vectors queen + man - woman = ?
model.wv.most_similar_cosmul(positive=['queen','man'], negative=['woman'])

#Finding the odd word out from the list of words given
print(model.wv.doesnt_match("man woman car".split()))
