from gensim.models import Word2Vec
from cosine_distance import cosine_similarity;

model = Word2Vec.load('./modelfile/MyModel')

print("----------length----------")
print(len(model.wv.vocab))

print("----------wmdistance----------")
print(model.wmdistance("image editing","image manipulation"))
print(model.wmdistance("computer","human"))

print("----------cos----------")
print(cosine_similarity(model['editing'],model['manipulation']))
print(cosine_similarity(model["computer"],model["human"]))