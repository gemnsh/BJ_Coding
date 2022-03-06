import sys
N= int(sys.stdin.readline())
a=[int(sys.stdin.readline()) for _ in range(N)]
chbin=[0]*8001
min_1,max_1=4001,-4001
a.sort()
result=[0]*4
result[0]=round(sum(a)/N)
result[1]=a[N//2]
for i in range(N):
    chbin[a[i]+4000]+=1
    if a[i]<min_1:
        min_1=a[i]
    if a[i]>max_1:
        max_1=a[i]
tmp=0
check=True
for i in range(8001):
    if tmp<chbin[i]:
        tmp=chbin[i]
        result[2]=i-4000
        check=True
    elif check==True and tmp==chbin[i]:
        tmp=chbin[i]
        result[2]=i-4000
        check=False
result[3]=max_1-min_1
for i in result:
    print(i)
