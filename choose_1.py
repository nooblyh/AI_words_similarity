import pandas as pd
import numpy as np
from gensim.models import Word2Vec

model = Word2Vec.load('./modelfile/zh/gensim-model-6zsjp5z5')

f = pd.read_csv('word_frequency.csv')
f = np.array(f)
frequency = {}
for i in f:
    frequency[i[0]] = i[1]

with open('01_result','r') as pair_file:
    pairs = pair_file.read().splitlines()

count=0
delete_word = []

for pair in pairs:
    pair = pair.split(",")
    pair_list_0 = pair[0].split()
    pair_list_1 = pair[1].split()
    length_0 = len(pair_list_0)
    length_1 = len(pair_list_1)
    if frequency[pair[0]] > frequency[pair[1]]:
        delete_word.append(pair[1])
    elif frequency[pair[0]] < frequency[pair[1]]:
        delete_word.append(pair[0])
    elif frequency[pair[0]] == frequency[pair[1]] and length_0 == length_1:
        for w in range(1,length_0):
            if not pair_list_0[length_0-w] in model or not pair_list_1[length_0-w] in model:
                continue
            else:
                if model.wv.vocab[pair_list_0[length_0-w]].count > model.wv.vocab[pair_list_1[length_0-w]].count:
                    delete_word.append(pair[1])
                    end = True
                    break
                else:
                    delete_word.append(pair[0])
                    end = True
                    break
    else:
        print("搞不定这对",pair[0],pair[1])
        count+=1

with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()
for i in delete_word:
    if i in words:
        words.remove(i)
to = open("words_final.txt",'w',encoding="UTF-8")
for w in words:
    to.write(w+"\n")
to.close()
#print(delete_word)
print(count)