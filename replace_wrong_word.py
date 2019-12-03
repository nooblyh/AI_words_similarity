import enchant
d = enchant.Dict("en_US")

from gensim.models import Word2Vec
model = Word2Vec.load('./modelfile/gensim-model-6zsjp5z5')

to = open("new_words_except_wrong.txt",'w',encoding="UTF-8")


with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()
for word in words:
    flag = True 
    word = word.split()
    for i in word:
        if i not in model:
            flag = False
            break

    if flag:
        new = []
        for i in word:
            true = i
            if(d.check(true)):
                new.append(true)
            else:
                for s,_ in model.wv.most_similar(i,topn=5):
                    if d.check(s):
                        true = s
                        print("INFO!"+ i + "改为" + true)
                        break
                new.append(true)
                if(true == i):
                    print("WARNING!"+ true + "的同义词也是错词")
        to.write(" ".join(str(i) for i in new)+"\n")
to.close()