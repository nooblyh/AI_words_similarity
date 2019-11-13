from load_words import find_similar
from by_cosine  import  contains
from gensim.models import Word2Vec

model = Word2Vec.load('./modelfile/MyModel')
with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()
    find_similar(words,model)