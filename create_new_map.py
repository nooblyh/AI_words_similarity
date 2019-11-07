from gensim.models import Word2Vec

threshold = 5
model = Word2Vec.load('./modelfile/MyModel')
trans_file = open("transfer_word.txt","r")
trans_words = trans_file.read().splitlines()
with open("dict.txt","r") as dict_file:
    with open("words.txt","r") as words_file:
        words = words_file.read().splitlines()
        dict_words = dict_file.read().splitlines()
        for w in words:
            print("\""+w+"\"", end = "")
            tmp = []

            for t_w in trans_words:
                index = t_w.index("/")
                if model.wmdistance(t_w[0:index],w) < threshold:
                    break
                elif model.wmdistance(t_w[index+1:],w) < threshold:
                    w = t_w[0:index]
                    tmp.append(t_w[0:index])
                else:
                    continue
                    
        
            for d_w in dict_words:
                if model.wmdistance(d_w,w) < threshold:
                    tmp.append(d_w)

            for d_w in tmp:
                print(",\""+d_w+"\"", end = "")
            print()
            
trans_file.close()

