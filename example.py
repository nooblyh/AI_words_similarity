from gensim.models import Word2Vec
from cosine_distance import cosine_similarity
from nltk.corpus import stopwords

model = Word2Vec.load('./modelfile/MyModel')
trans_file = open("transfer_word.txt","r")
trans_words = trans_file.read().splitlines()
words = ["machine learning","transfer learning","back propagation","cnn","rnn","lstm","attention"]
stopwords = stopwords.words('english')
threshold = 5
with open("dict.txt","r") as dict_file:
    dict_words = dict_file.read().splitlines()
    for w in words:
            print("\""+w+"\"", end = "")
            w = w.lower().split()
            w = [i for i in w if i not in stopwords]
            tmp = []

            for t_w in trans_words:
                index = t_w.index("/")
                t_w_origin = t_w[0:index].lower().split()
                t_w_origin = [i for i in t_w_origin if i not in stopwords]
                t_w_abbr = t_w[index+1:].lower().split()
                t_w_abbr = [i for i in t_w_abbr if i not in stopwords]
                if model.wmdistance(t_w_origin,w) == 0:
                    continue
                elif model.wmdistance(t_w_abbr,w) == 0:
                    w = t_w_origin
                    tmp.append(w)
                elif model.wmdistance(t_w_origin,w) < threshold or model.wmdistance(t_w_abbr,w) < threshold:
                    tmp.append(t_w_origin)
                    
        
            for d_w in dict_words:
                d_w = d_w.lower().split()
                d_w = [i for i in d_w if i not in stopwords]
                if d_w == w:
                    continue
                if model.wmdistance(d_w,w) < threshold:
                    tmp.append(d_w)

            for d_w in tmp:
                print(",\"%s\""%(" ".join(str(i) for i in d_w)), end = "")
            print()
        

'''
print("----------length----------")
print(len(model.wv.vocab))

print("----------wmdistance----------")
print("image editing and image manipulation")
print(model.wmdistance("image editing","image manipulation"))
print("transaction processing and transactional process")
print(model.wmdistance("transaction processing","transactional process"))
print("support vector machines and support vector machine")
print(model.wmdistance("support vector machines","support vector machine"))
print("radial basis functional and radial basis functions")
print(model.wmdistance("radial basis functional","radial basis functions"))
print("computer and in")
print(model.wmdistance("computer","in"))

print("----------cos----------")
print(cosine_similarity(model['editing'],model['manipulation']))
print(cosine_similarity(model["computer"],model["human"]))
'''