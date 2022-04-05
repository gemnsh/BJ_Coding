N=int(input())
stair=[int(input())for _ in range(N)]+[0,0,0]

d=[0]*(N+3)
d[0]=stair[0]
d[1]=stair[0]+stair[1]
d[2]=max(stair[1],stair[0])+stair[2]
for i in range(3,N):
    d[i]=max(d[i-3]+stair[i-1],d[i-2])+stair[i]
print(d[N-1])