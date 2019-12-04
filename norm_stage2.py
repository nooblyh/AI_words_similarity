from load_words import find_similar
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import pandas as pd
import numpy as np

def same_words(lw1,lw2,stemmer):
    for i in range(0,len(lw1)):
        if stemmer.stem(lw1[i]) != stemmer.stem(lw2[i]):
            return False
    return True


if __name__ == "__main__":
    '''
    f = pd.read_csv('word_frequency.csv')
    f = np.array(f)
    frequency = {}
    for i in f:
        frequency[i[0]] = i[1]
    '''

    stemmer = PorterStemmer()
    to = open("words_choose_by_hand.txt",'w',encoding="UTF-8")
    with open("words.txt","r") as words_file:
        words = words_file.read().splitlines()

    i=0

    while i<len(words):
        j=i+1
        while j<len(words):
            w1 = words[i]
            w2 = words[j]
            lw1 = w1.split()
            lw2 = w2.split()
            if len(lw1) == len(lw2) and same_words(lw1,lw2,stemmer):
                print(w1+"\t"+w2)
                to.write(w1+"\t"+w2+"\n")
                '''
                if frequency[w1] == frequency[w2] ==0:
                    print("两个词都不存在")
                if frequency[w1] < frequency[w2]:
                    print("选择%s,删去%s"%(w2,w1))
                    words.remove(w1)
                    i = i-1
                    break
                else:
                    print("选择%s,删去%s"%(w1,w2))
                    words.remove(w2)
                    j = j-1
                '''
            j = j+1
        i = i+1
    to.close()
    '''
    to = open("new_words_by_stem.txt",'w',encoding="UTF-8")
    for w in words:
        to.write(w+"\n")
    '''