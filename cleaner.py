import json
import itertools
from load_words import  word_count
from gensim.models import Word2Vec

words = []
with open("./db5.json",'r') as load_f:
    load_dict = json.load(load_f)
    for key in load_dict:
        words.append(key)

list = {}
model = Word2Vec.load('./modelfile/MyModel')
shrehold = 0.1

ls = itertools.combinations(words, 2)
for l in ls:
    disctance = model.wmdistance(l[0],l[1])
    list[l] = disctance

print(list[1:100])