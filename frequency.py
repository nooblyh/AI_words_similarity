from get_data import get_data

sentences = []
text = get_data()
for l in text:
    sentence = " ".join(str(w) for w in l)
    sentences.append(sentence)
with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()
for word in words:
    count = 0
    for s in sentences:
        if word in s:
            count += 1
    print("\"" + word + "\"," + str(count))
