n=int(input())
lst=[[],[],[],[],[]]
for i in range(n):
    a=list(map(int,input().split()))
    lst[0].append(a[0])
    lst[1].append(a[1])
    lst[2].append(a[2])
    lst[3].append(a[3])
    lst[4].append(a[4])
mate=[set() for _ in range(n)]
for i in range(5):
    for j in range(n):
        for k in range(j,n):
            if lst[i][j]==lst[i][k] and j!=k:
                mate[j].add(k+1)
                mate[k].add(j+1)
result=[0,-1]
for i in range(len(mate)):
    if result[0]<len(mate[i]):
        result[0]=len(mate[i])
        result[1]=i+1

print(result[1]if result[0]>1 else 1)