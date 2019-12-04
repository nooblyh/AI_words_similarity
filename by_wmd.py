from gensim.models import Word2Vec
from nltk.corpus import stopwords
import Levenshtein 

threshold = 0.9
model = Word2Vec.load('./modelfile/gensim-model-6zsjp5z5')
trans_file = open("transfer_word.txt","r")
trans_words = trans_file.read().splitlines()

stopwords = stopwords.words('english')

with open("dict.txt","r") as dict_file:
    with open("words.txt","r") as words_file:
        words = words_file.read().splitlines()
        dict_words = dict_file.read().splitlines()
        for w in words:
            w = w.lower().split()
            w = [i for i in w if i not in stopwords]
            tmp = []

            for t_w in trans_words:
                index = t_w.index("/")
                t_w_origin = t_w[0:index].lower().split()
                t_w_origin = [i for i in t_w_origin if i not in stopwords]
                t_w_abbr = t_w[index+1:].lower().split()
                t_w_abbr = [i for i in t_w_abbr if i not in stopwords]

                flag = 0
                for x in t_w_origin:
                    if x not in model:
                        flag = 1
                if flag == 1:
                    continue

                if t_w_origin == w:
                    continue
                elif t_w_abbr == w:
                    w = t_w_origin
                    tmp.append(w)
                    continue
                else:
                    flag = 0
                    for x in t_w_abbr:
                        if x not in model:
                            flag = 1
                    if flag == 1:
                        continue

                if Levenshtein.seqratio(t_w_origin,w) > threshold or Levenshtein.seqratio(t_w_abbr,w) > threshold:
                    tmp.append(t_w_origin)
                    
        
            for d_w in dict_words:
                d_w = d_w.lower().split()
                d_w = [i for i in d_w if i not in stopwords]

                flag = 0
                for x in d_w:
                    if x not in model:
                        flag = 1
                if flag == 1:
                    continue

                if d_w == w:
                    continue
                if Levenshtein.seqratio(d_w,w) > threshold:
                    tmp.append(d_w)
            if(tmp):
                for d_w in tmp:
                    print("\""+w+"\"", end = "")
                    print(",\"%s\""%(" ".join(str(i) for i in d_w)), end = "")
                print()
            
trans_file.close()