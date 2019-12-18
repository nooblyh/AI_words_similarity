import pandas as pd
import numpy as np
from gensim.models import Word2Vec

model = Word2Vec.load('./modelfile/zh/gensim-model-6zsjp5z5')

f = pd.read_csv('word_frequency.csv')
f = np.array(f)
frequency = {}
for i in f:
    frequency[i[0]] = i[1]

wcbh = pd.read_csv('words_choose_by_hand.csv')
wcbh = np.array(wcbh)
count=0
delete_word = []

for pair in wcbh:
    pair_list_0 = pair[0].split()
    pair_list_1 = pair[1].split()
    length = len(pair_list_0)
    i = length
    end = False
    while(i>=0 and not end):
        for ii in range(0,length - i + 1):
            a = " ".join([x for x in pair_list_0[ii:i]])
            b = " ".join([x for x in pair_list_1[ii:i]])
            if not a in frequency or not b in frequency:
                continue
            if frequency[a] == frequency[b] == 0:
                continue
            elif frequency[a] > frequency[b]:
                delete_word.append(pair[1])
                end = True
                break
            else:
                delete_word.append(pair[0])
                end = True
                break
        i-=1

    if not end:
        for w in range(1,length):
            if not pair_list_0[length-w] in model or not pair_list_1[length-w] in model:
                continue
            else:
                if model.wv.vocab[pair_list_0[length-w]].count > model.wv.vocab[pair_list_1[length-w]].count:
                    delete_word.append(pair[1])
                    end = True
                    break
                else:
                    delete_word.append(pair[0])
                    end = True
                    break


    if not end:
        print("搞不定这对",pair[0],pair[1])
        count+=1

with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()
for i in delete_word:
    if i in words:
        words.remove(i)
to = open("words_v1.txt",'w',encoding="UTF-8")
for w in words:
    to.write(w+"\n")
to.close()
#print(delete_word)
print(count)

