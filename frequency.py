from get_data import get_data

def n_slices(n, list_):
    for i in range(len(list_) + 1 - n):
        yield list_[i:i+n]

def isSublist(list_, sub_list):
    for slice_ in n_slices(len(sub_list), list_):
        if slice_ == sub_list:
            return True
    return False
    
sentences = []
text = get_data()
for l in text:
    sentences.append(l)
with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()
for word in words:
    word = word.split()
    count = 0
    for s in sentences:
        if isSublist(s,word):
            count += 1
    print("\"" + word + "\"," + str(count))

