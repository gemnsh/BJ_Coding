from math import gcd

N=int(input())
truck=[int(input()) for _ in range(N)]
truck.sort()
a=[0]*(N-1)
for i in range(N-1):
    a[i]=truck[i+1]-truck[i]
result=a[0]
for i in range(1,N-1):
    result=gcd(result,a[i])
for i in range(2,result):
    if result%i==0:
        print(i,end=' ')
print(result)