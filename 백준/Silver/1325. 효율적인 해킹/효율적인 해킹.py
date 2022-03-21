import sys
from collections import deque
def bfs(num):
    visited=[False]*(N+1)
    q=deque([num])
    visited[num]=True
    return_value=1
    while q:
        t=q.popleft()
        for i in trust[t]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                return_value+=1
    return return_value

N, M=map(int,sys.stdin.readline().split())
max_com=0
com=[]
trust=[[]for _ in range(N+1)]
for i in range(M):
    tmp=list(map(int,sys.stdin.readline().split()))
    trust[tmp[1]].append(tmp[0])
for i in range(1,N+1):
    now=bfs(i)
    if now>max_com:
        com=[]
        com.append(i)
        max_com=now
    elif now==max_com:
        com.append(i)
print(*com)