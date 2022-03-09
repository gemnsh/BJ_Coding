n=int(input())
result=0
a=[]
for i in range(0,n+1):
    data=[n]
    data.append(i)
    while data[-1]<=data[-2]:
        data.append(data[-2]-data[-1])
    tmp=len(data)
    if tmp>=result:
        result=tmp
        a=data[:]
print(result)
print(*a)