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

def generate_pair(words,model):
    ls = itertools.combinations(words, 2)
    for l in ls:
        print(l)
        print(model.wmdistance(l[0],l[1]))
        
if __name__ == "__main__":
    words = get_relative_words("deep learning")
    model = Word2Vec.load('./modelfile/MyModel')
    generate_pair(words,model)