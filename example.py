from gensim.models import Word2Vec
from cosine_distance import cosine_similarity

model = Word2Vec.load('./modelfile/MyModel')

words = ["machine learning","transfer learning","back propagation"]
threshold = 5
with open("dict.txt","r") as dict_file:
    dict_words = dict_file.read().splitlines()
    for w in words:
        print("\""+w+"\"", end = "")
        tmp = []
        for d_w in dict_words:
            if("/" in d_w):
                index = d_w.index("/")
                if model.wmdistance(d_w[0:index],w) < threshold or model.wmdistance(d_w[index+1:],w) < threshold:
                    tmp.append(d_w[0:index])
            else:
                if model.wmdistance(d_w,w) < threshold:
                    tmp.append(d_w)         
        for d_w in tmp:
            print(",\""+d_w+"\"", end = "")
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