from collections import deque
N,M=map(int,input().split())
floor=[input() for _ in range(N)]
visited=[[0 for _ in range(M)] for _ in range(N)]
dy=[0,0,-1,1]
dx=[1,-1,0,0]

def bfs(y,x):
    q=deque([[y,x]])
    while q:
        tmp=q.popleft()
        for i in range(4):    
            tmpY=dy[i]+tmp[0]
            tmpX=dx[i]+tmp[1]
            if 0<=tmpX<M and 0<=tmpY<N:
                if visited[tmpY][tmpX]==0:
                    if floor[tmpY][tmpX]==floor[tmp[0]][tmp[1]]:
                        if (floor[tmpY][tmpX]=='-' and dy[i]==0) or (floor[tmpY][tmpX]=='|' and dx[i]==0):
                            visited[tmpY][tmpX]=1
                            q.append([tmpY,tmpX])
result=0
for i in range(N):
    for j in range(M):
        if visited[i][j]==0:
            bfs(i,j)
            result+=1
print(result)