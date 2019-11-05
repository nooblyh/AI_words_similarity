from get_data import get_data
from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from cosine_distance import cosine_similarity;

text = get_data()
model = Word2Vec(text, size=100, window=5, min_count=1, workers=4)
model.save('./MyModel')
model.wv.save_word2vec_format('./mymodel.txt', binary=False)
print('linear' in model.wv.vocab)
print(len(model.wv.vocab))
print(model.wmdistance("image editing","image manipulation"))
print(model.wmdistance("computer","human"))

print("----------cos----------")
print(cosine_similarity(model['editing'],model['manipulation']))
print(cosine_similarity(model["image editing"],model["image manipulation"]))
print(cosine_similarity(model["computer"],["human"]))