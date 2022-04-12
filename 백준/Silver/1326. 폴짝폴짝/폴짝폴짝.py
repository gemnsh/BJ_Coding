from collections import deque
dx=[1,-1]
def check(A,B):
    visited=[-1]*N
    visited[A]=0
    q=deque([A])
    while q:
        tmp=q.popleft()
        for i in range(2):
            for j in range(1,N//dari[tmp]+1):
                t=tmp+dari[tmp]*j*dx[i]
                if 0<=t<N and visited[t]==-1:
                    q.append(t)
                    visited[t]=visited[tmp]+1
                if visited[B]!=-1:
                    return visited[B]
    return -1
N=int(input())
dari=list(map(int,input().split()))
a,b=map(int,input().split())
print(check(a-1,b-1))