cnt=int(input())
result=[]
for _ in range(cnt):
    tmp=int(input())
    if tmp==0:
        result.pop()
    else:
        result.append(tmp)
answer=0
for i in  range(len(result)):
    answer+=result[i]
print(answer)