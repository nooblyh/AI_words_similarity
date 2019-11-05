import json
import itertools
from gensim.models import Word2Vec

def get_relative_words(word):
    with open("./db5.json",'r') as load_f:
        load_dict = json.load(load_f)
        words_data = json.loads(load_dict[word]["value"])['data']['up'] + json.loads(load_dict[word]["value"])['data']['down']
        words = []
        for key in words_data:
            words.append(key["name"])
        return words

def get_vectors(words,model):
    vectors = {}
    for word in words:
        if word in model:
            vectors[word] = model[word]
    print(vectors)
    return vectors

def generate_pair(vectors):
    ls = itertools.combinations(vectors, 2)
    for l in ls:
        print(l)
        
if __name__ == "__main__":
    words = get_relative_words("deep learning")
    model = Word2Vec.load('./modelfile/MyModel')
    vectors = get_vectors(words,model)
    generate_pair(vectors)