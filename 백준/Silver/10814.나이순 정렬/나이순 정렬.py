T=int(input())
data=[]
for i in range(0,T):
    data.append(input().split())
data.sort(key=lambda  x:int(x[0]))
for result in data:
    print(*result)