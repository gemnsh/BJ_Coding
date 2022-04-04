def combi(arr,n):
    if n==0:
        return[[]]
    data=[]
    for i in range(len(arr)):
        tmp=arr[i+1:]
        for j in combi(tmp,n-1):
            data.append([arr[i]]+j)
    return data

N,M=map(int,input().split())
lst=list(range(1,N+1))
k=combi(lst,M)
for i in k:
    print(*i)