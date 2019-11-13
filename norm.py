from load_words import find_similar
from gensim.models import Word2Vec
from nltk.stem import WordNetLemmatizer

def same_words(lw1,lw2):
    for i in range(0,len(lw1)):
        if wnl.lemmatize(lw1[i]) != wnl.lemmatize(lw2[i]):
            return False
    return True


if __name__ == "__main__":
    wnl = WordNetLemmatizer()
    model = Word2Vec.load('./modelfile/MyModel')
    threshold = 2.0

    with open("words.txt","r") as words_file:
        words = words_file.read().splitlines()

    i=0

    for w1 in words:
        j=i+1
        while j<len(words):
            w2 = words[j]
            lw1 = w1.split()
            lw2 = w2.split()
            if len(lw1) == len(lw2) and same_words(lw1,lw2):
                print(w1+"\t"+w2)
                words.pop(j)
                j=j-1
            j=j+1
        i=i+1
        
    to = open("new_words.txt",'w',encoding="UTF-8")
    for w in words:
        to.write(w+"\n")