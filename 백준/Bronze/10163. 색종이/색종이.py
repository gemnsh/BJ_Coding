data=[[0 for _ in range(1002)]for _ in range(1002)]
T=int(input())
a=[]
result=[]
for t in range(T):
    a.append(list(map(int,input().split())))
for k in range(T-1,-1,-1):
    ta=a[k]    
    tmp=0
    for i in range(ta[0],ta[2]+ta[0]):
        for j in range(ta[1],ta[3]+ta[1]):
            if data[i][j]==0:
                data[i][j]=1
                tmp+=1
    result.append(tmp)
for i in range(T-1,-1,-1):
    print(result[i])