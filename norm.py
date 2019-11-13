from load_words import find_similar
from gensim.models import Word2Vec

model = Word2Vec.load('./modelfile/MyModel')
threshold = 2.0

with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()

i=0

for w1 in words:
    j=i+1
    while j<len(words):
        w2 = words[j]
        disctance = model.wmdistance(w1,w2)
        if threshold > disctance:
            print(w1+"\t"+w2)
            print(disctance)
            words.pop(j)
            j=j-1
        j=j+1
    i=i+1
    
to = open("new_words.txt",'w',encoding="UTF-8")
for w in words:
    to.write(w+"\n")