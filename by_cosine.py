from gensim.models import Word2Vec
from cosine_distance import cosine_similarity
from nltk.corpus import stopwords

model = Word2Vec.load('./modelfile/MyModel')
trans_file = open("transfer_word.txt","r")
trans_words = trans_file.read().splitlines()
# words = ["machine learning","transfer learning","back propagation","cnn","rnn","lstm","attention","gymnastic"]
stopwords = stopwords.words('english')
threshold = 0.5

with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()
    with open("dict.txt","r") as dict_file:
        dict_words = dict_file.read().splitlines()
        for w in words:
            print("\""+w+"\"", end = "")
            w = w.lower().split()
            w = [i for i in w if i not in stopwords]
            tmp = []

            for t_w in trans_words:
                index = t_w.index("/")
                t_w_origin = t_w[0:index]
                t_w_abbr = t_w[index+1:]
                t_w_origin = t_w_origin.lower().split()
                t_w_origin = [i for i in t_w_origin if i not in stopwords]
                t_w_abbr = t_w_abbr.lower().split()
                t_w_abbr = [i for i in t_w_abbr if i not in stopwords]
                if t_w_origin == w:
                    continue
                elif t_w_abbr == w:
                    flag = 0
                    for x in t_w_origin:
                        if x not in model:
                            flag = 1
                    if flag == 1:
                        continue
                    w = t_w_origin
                    tmp.append(w)

            for t_w in trans_words:
                index = t_w.index("/")
                t_w_origin = t_w[0:index]
                t_w_abbr = t_w[index+1:]
                t_w_origin = t_w_origin.lower().split()
                t_w_origin = [i for i in t_w_origin if i not in stopwords]
                t_w_abbr = t_w_abbr.lower().split()
                t_w_abbr = [i for i in t_w_abbr if i not in stopwords]
                    
                flag = 0
                for x in t_w_origin:
                    if x not in model:
                        flag = 1
                for x in t_w_abbr:
                    if x not in model:
                        flag = 1
                if flag == 1:
                    continue

                if model.n_similarity(t_w_origin,w) > threshold or model.n_similarity(t_w_abbr,w) > threshold:
                    tmp.append(t_w_origin)
                
    
            for d_w in dict_words:
                d_w = d_w.lower().split()
                d_w = [i for i in d_w if i not in stopwords]
                if d_w == w or d_w == []:
                    continue

                flag = 0
                for x in d_w:
                    if x not in model:
                        flag = 1
                if flag == 1:
                    continue

                if model.n_similarity(d_w,w) > threshold:
                    tmp.append(d_w)

            for d_w in tmp:
                print(",\"%s\""%(" ".join(str(i) for i in d_w)), end = "")
            print()