cnt=int(input())
count=0
for i in range(cnt):
    word=input()
    n=set()
    while len(word)>0:
        if word[0] not in n:
            n.add(word[0])
            word=word.lstrip(word[0])
        else :
            count+=1
            break
print(cnt-count)