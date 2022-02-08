num=list(map(int,input().split()))
joseph=[i for i in range(1,num[0]+1)]
cnt=0
result=[]
a=0
while len(joseph):
    if a>=len(joseph):
        a-=len(joseph)
    if cnt==num[1]-1:
        cnt=0
        result.append(joseph.pop(a))
    else:
        a+=1
        cnt+=1
print((str(result).replace('[','<')).replace(']','>'))