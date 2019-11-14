from get_data import get_data

text = get_data()
with open("words.txt","r") as words_file:
    words = words_file.read().splitlines()
for word in words:
    count = 0
    for s in text:
        sentence = " ".join(str(w) for w in s)
        if word in sentence:
            count += 1
    print("\""+word+"\","+count)