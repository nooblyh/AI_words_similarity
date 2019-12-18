import Levenshtein 

result = []
with open("words_v2.txt","r") as words_file:
    words = words_file.read().splitlines()
    i = 0
    for w1 in words:
        result.append([])
        for w2 in words:
            if (len(w1.split())==1 and len(w2.split())>1):
                head = ""
                for x in w2.split():
                    head = head + x[0]
                result[i].append(Levenshtein.seqratio(w1,head))
                if(Levenshtein.seqratio(w1,head)>0.8):
                    print(w1,w2)
            elif (len(w1.split())>1 and len(w2.split())==1):
                head = ""
                for x in w1.split():
                    head = head + x[0]
                result[i].append(Levenshtein.seqratio(head,w2))
                if(Levenshtein.seqratio(head,w2)>0.8):
                    print(w1,w2)
            else:
                result[i].append(0)
        i+=1
print(result)
with open("matrix.txt","w") as f:
    for i in range(len(result)):
        for j in range(len(result)):
            f.write(str(result[i][j]))
            f.write(" ")
        f.write("\n")