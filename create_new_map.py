from gensim.models import Word2Vec

model = Word2Vec.load('./modelfile/MyModel')
with open("spec.txt","r") as dict_file:
    with open("words.txt","r") as words_file:
        words = words_file.read().splitlines()
        for w in words:
            print(w+":")
            for d_w in dict_file:
                if("/" in d_w):
                    index = d_w.index("/")
                    if model.wmdistance(d_w[0:index],w) < 5 or model.wmdistance(d_w[index+1:],w) < 5:
                        print(d_w[0,index])
                else:
                    if model.wmdistance(d_w,w) < 5:
                        print(d_w)

