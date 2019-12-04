from get_data import get_data

def is_sublist(sublst, lst): return sum([lst == sublst[i: i + len(lst)] for i in range(len(sublst) - len(lst))]) > 0

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
        if is_sublist(s,word):
            count += 1
    print("\"" + " ".join(str(i) for i in word) + "\"," + str(count))
