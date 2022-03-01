T=int(input())
d=[0]*10
while T//10>=1:
    tmp=T%10
    T=T//10
    d[tmp]+=1
d[T]+=1
for i in range(9,-1,-1):
    while d[i]>0:
        print(i,end='')
        d[i]-=1