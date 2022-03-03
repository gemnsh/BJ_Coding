data=list(map(int,input().split()))
tree=list(map(int,input().split()))
start,end=0,max(tree)
while start<=end:
    tmp=(start+end)//2
    cnt=0
    for i in range(data[0]):
        if tree[i]-tmp>0:
            cnt+=tree[i]-tmp
    if cnt>=data[1]:
        start=tmp+1
    elif cnt<data[1]:
        end=tmp-1
print(end)