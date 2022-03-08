import sys
N=int(input())
a=list(map(int,sys.stdin.readline().split()))
b=sorted(set(a))
result={}
c=[]
for i in range(len(b)):
    result[b[i]]=i
for i in range(len(a)):
    c.append(result[a[i]])
print(*c)