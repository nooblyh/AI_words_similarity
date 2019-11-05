from gensim.models import Word2Vec
from cosine_distance import cosine_similarity;

model = Word2Vec.load('./modelfile/MyModel')

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