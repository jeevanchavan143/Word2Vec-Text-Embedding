# Word2Vec-Text-Embedding

Libraries Used: nltk , pandas , gensim
Dataset : From Kaggle Open Source 
Link to dataset : https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

In this Project I used word2vec for text embedding.

Text embeddings are the mathematical representations of words as vectors.

The text embedding  transforms text into a Vecors ( numerical representation) (an embedding)
If two words or documents have a similar embedding, they are semantically similar.
For example,
“anchor” and “boat” have close embeddings, while “anchor” and “koala” do not. Similarly,
the same word in different languages like “amore” and “love” have close embeddings

Machine learning algorithms deals with numeric data only. 
It can not handle string / text data.

Word2Vec used to convert text data into corresponding numeric representation also known as vector

3 main algorithms for learning a word embedding from text data. 

1. Embedding Layer 

It requires that document text be cleaned and prepared such that each word is one-hot encoded. The size of the vector space is specified as part of the model, such as 50, 100, or 300 dimensions. The vectors are initialized with small random numbers. The embedding layer is used on the front end of a neural network and is fit in a supervised way using the Backpropagation algorithm. This approach of learning an embedding layer requires a lot of training data and can be slow, but will learn an embedding both targeted to the specific text data and the NLP task. 

2. Word2Vec 

Word2Vec is a statistical method for efficiently learning a standalone word embedding from a text corpus. 
Word2vec is a group of related models that are used to produce word embeddings. These models are shallow, two-layer neural networks that are trained to reconstruct linguistic contexts of words. Word2vec takes as its input a large corpus of text and produces a vector space, typically of several hundred dimensions, with each unique word in the corpus being assigned a corresponding vector in the space. Word vectors are positioned in the vector space such that words that share common contexts in the corpus are located close to one another in the space

3. GloVe 

The Global Vectors for Word Representation, or GloVe, algorithm is an extension to the word2vec method for efficiently learning word vectors 

This will require a large amount of text data to ensure that useful embeddings are learned, such as millions or billions of words. 



