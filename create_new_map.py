from gensim.models import Word2Vec

threshold = 5
model = Word2Vec.load('./modelfile/MyModel')
with open("dict.txt","r") as dict_file:
    with open("words.txt","r") as words_file:
        words = words_file.read().splitlines()
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

