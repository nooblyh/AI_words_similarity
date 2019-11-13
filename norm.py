from load_words import find_similar
from gensim.models import Word2Vec

model = Word2Vec.load('./modelfile/MyModel')
threshold = 2.0

with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()

for i in range(0,len(words)):
    for j in range(i+1,len(words)):
        disctance = model.wmdistance(words[i],words[j])
        if threshold > disctance:
            print(words[i]+'\t'+words[j])
            print(disctance)
            words.pop(j)
            j=j-1