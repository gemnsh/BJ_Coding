K,N=map(int,input().split())
data=[]
for _ in range(K):
    data.append(int(input()))
start=1
end=max(data)
while start<=end:
    tmp=(start+end)//2
    cnt=0
    for i in range(K):
        cnt+=data[i]//tmp
    if cnt<N:
        end=tmp-1
    elif cnt>=N:
        start=tmp+1
print(end)