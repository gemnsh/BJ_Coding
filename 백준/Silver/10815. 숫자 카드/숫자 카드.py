def b_search(start,end,num):
    while start<=end:
        tmp=(start+end)//2
        if n_1[tmp]==num:
            return 1
        elif n_1[tmp]>num:
            return b_search(start,tmp-1,num)
        else:
            return b_search(tmp+1,end,num)
    return 0
N=int(input())
n_1=sorted(list(map(int,input().split())))
M=int(input())
n_2=list(map(int,input().split()))
data=[True]*M
for i in range(M):
    data[i]=b_search(0,N-1,n_2[i])
print(*data)