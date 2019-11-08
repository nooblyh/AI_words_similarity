from gensim.models import Word2Vec
from nltk.corpus import stopwords

threshold = 5
model = Word2Vec.load('./modelfile/MyModel')
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
            print("\""+w+"\"", end = "")
            tmp = []

            for t_w in trans_words:
                index = t_w.index("/")
                t_w_origin = t_w[0:index].lower().split()
                t_w_origin = [i for i in t_w_origin if i not in stopwords]
                t_w_abbr = t_w[index+1:].lower().split()
                t_w_abbr = [i for i in t_w_abbr if i not in stopwords]
                if model.wmdistance(t_w_origin,w) < threshold:
                    break
                elif model.wmdistance(t_w_abbr,w) < threshold:
                    w = t_w_origin
                    tmp.append(w)
                else:
                    continue
                    
        
            for d_w in dict_words:
                d_w = w.lower().split()
                d_w = [i for i in d_w if i not in stopwords]
                if d_w == w:
                    continue
                if model.wmdistance(d_w,w) < threshold:
                    tmp.append(d_w)

            for d_w in tmp:
                print(",\""+d_w+"\"", end = "")
            print()
            
trans_file.close()