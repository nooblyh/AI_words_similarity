from get_data import get_data


def is_sublist(l,s):
    if s==[]:
        return True
    elif s==l:
        return True
    elif len(s)>len(l):
        return False
    else:
        for i in range(len(l)):
            if l[i]==s[0]:
                if i==len(l)-1 and len(s)>1:
                    return False
                else:
                    n=1
                    while (l[n+i]==s[n])and(n<len(s)):
                        n+=1
                        if n==len(s):
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
        if is_sublist(s,word):
            count += 1
    print("\"" + " ".join(str(i) for i in word) + "\"," + str(count))
