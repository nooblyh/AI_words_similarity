from get_data import get_data

def is_subset(s,w):
    if w not in s:
        return False
    if s.index(w) + len(w) == len(s) or s[s.index(w) + len(w)] == " ":
        return True
    else:
        return False

sentences = []
text = get_data()
for l in text:
    sentences.append(l)
with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()
for word in words:
    count = 0
    for s in sentences:
        if is_subset(" ".join(str(i) for i in s),word):
            count += 1
    print("\"" + word + "\"," + str(count))
