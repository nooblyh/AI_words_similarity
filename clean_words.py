import pandas as pd
import numpy as np

from gensim.models import Word2Vec

model = Word2Vec.load('./modelfile/zh/gensim-model-6zsjp5z5')
new_words=[]
non_words=[]


with open("words_v1.txt","r") as words_file:
    words = words_file.read().splitlines()
    for word in words:
        accept = True
        word_list = word.split()
        for w in word_list:
            if w not in model:
                non_words.append(word)
                accept = False
                break
            else:
                continue
        if accept:
            new_words.append(word)
                    
print(len(non_words))

to = open("words_v2.txt",'w',encoding="UTF-8")
for w in new_words:
    to.write(w+"\n")
to.close()
