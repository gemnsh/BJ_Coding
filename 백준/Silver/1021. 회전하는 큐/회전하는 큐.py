from collections import deque
N,M=map(int,input().split())
a=deque(range(1,N+1))
data=list(map(int,input().split()))
result=0
for d in data:
    if a[0]!=d:
        if a.index(d)>len(a)-a.index(d):
            result+=len(a)-a.index(d)
            for i in range(len(a)-a.index(d)):
                tmp=a.pop()
                a.appendleft(tmp)
        else:
            result+=a.index(d)
            for i in range(a.index(d)):
                tmp=a.popleft()
                a.append(tmp)
    a.popleft()
print(result)