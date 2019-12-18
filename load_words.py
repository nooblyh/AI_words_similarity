import json
import itertools
from gensim.models import Word2Vec

def get_center_words():
    words = []
    with open("./db5.json",'r') as load_f:
        load_dict = json.load(load_f)
        for key in load_dict:
            words.append(key)
    return words

def get_relative_words(word):
    with open("./db5.json",'r') as load_f:
        load_dict = json.load(load_f)
        words_data = json.loads(load_dict[word]["value"])['data']['up'] + json.loads(load_dict[word]["value"])['data']['down']
        words = []
        for key in words_data:
            words.append(key["name"])
        return words

def find_similar(words, model, threshold=2.0):
    ls = itertools.combinations(words, 2)
    for l in ls:
        disctance = model.wmdistance(l[0],l[1])
        if threshold > disctance:
            print(l)
            print(disctance)
            '''
            if(word_count(l[0]) > word_count(l[1])):
                print("choose %s"%l[0])
            else:
                print("choose %s"%l[1])
            '''
            

def word_count(word):
    sum = 0
    for w in word.split():
        if w in model:
            sum += model.wv.vocab[w].count
        else:
            print("!!!!!%s not exist!!!!!"%w)
    return sum

# example
if __name__ == "__main__":
    center_words=get_center_words()
    to = open("./words.txt","w",encoding="UTF-8")
    for center_word in center_words:
        to.write(center_word+"\n")
    '''
    with open("./db5.json",'r') as load_f:
        load_dict = json.load(load_f)
        for center_word in load_dict:
            words = get_relative_words(center_word)
            find_similar(words,model)
    '''
