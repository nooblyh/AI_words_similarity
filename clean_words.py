import pandas as pd
import numpy as np



with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()
    f = pd.read_csv('word_frequency.csv')
    f = np.array(f)
    for i in f:
        if i[1] == 0:
            words.remove(i[0])

to = open("new_words_all_exists.txt",'w',encoding="UTF-8")
for w in words:
    to.write(w+"\n")
to.close()