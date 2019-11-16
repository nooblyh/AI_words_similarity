from gensim.models import Word2Vec
from cosine_distance import cosine_similarity
from nltk.corpus import stopwords

model = Word2Vec.load('./modelfile/gensim-model-6zsjp5z5')
trans_file = open("transfer_word.txt","r")
trans_words = trans_file.read().splitlines()
# words = ["machine learning","transfer learning","back propagation","cnn","rnn","lstm","attention","gymnastic"]
stopwords = stopwords.words('english')
threshold = 0.7
N= 3  #指定的最多相似词个数


def contains(phrase):
    for x in phrase:
        if x not in model:
            return False
    return True

# 添加同义词，newterm为新匹配的同义词，newValue为相似度,termlist为已有的同义词列表
def add(termlist,newterm,newValve,count):

    if count < N:
        termlist.append([newterm,newValve])
        termlist.sort(key=lambda x:x[1],reverse=True)
    
    elif newValve < termlist[len(termlist)-2][1]:
        return count
    else:
        del(termlist[-1])
        termlist.append([newterm,newValve])
        termlist.sort(key=lambda x:x[1],reverse=True)

    return count+1

with open("new_words.txt","r") as words_file:
    words = words_file.read().splitlines()

with open("dict.txt","r") as dict_file:
    dict_words = dict_file.read().splitlines()
    
    for w in words:
        count = 1 
        
        print("\""+w+"\"", end = "")
        w = w.lower().split()
        w = [i for i in w if i not in stopwords]
        if not contains(w) or w ==[]:
            continue

        tmp = [[" ",0]]
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
                if not contains(t_w_origin):
                    continue
                w = t_w_origin
                tmp.append([w,1])
                count = count+1

        
        for t_w in trans_words:
            index = t_w.index("/")
            t_w_origin = t_w[0:index]
            t_w_abbr = t_w[index+1:]
            t_w_origin = t_w_origin.lower().split()
            t_w_origin = [i for i in t_w_origin if i not in stopwords]
            t_w_abbr = t_w_abbr.lower().split()
            t_w_abbr = [i for i in t_w_abbr if i not in stopwords]
                
            if not contains(t_w_origin) or not contains(t_w_abbr):
                continue

            if model.n_similarity(t_w_origin,w) > threshold or model.n_similarity(t_w_abbr,w) > threshold:    
                count = add(tmp,t_w_origin,model.n_similarity(t_w_origin,w),count)                    
                    
        
        for d_w in dict_words:
            d_w = d_w.lower().split()
            d_w = [i for i in d_w if i not in stopwords]
            if d_w == w or d_w == [] or not contains(d_w):
                continue

            if model.n_similarity(d_w,w) > threshold:
                count=add(tmp,d_w,model.n_similarity(d_w,w),count)
                

        
        for Item in tmp:
            if not ''.join(Item[0])==" ":
                print(",\"%s\""%(" ".join(str(i) for i in Item[0])) ,end="")
        
        
        print()