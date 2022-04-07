from collections import deque
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs():
    q=deque([[0,0,0]])
    visited=[[0 for _ in range(M)] for _ in range(N)]
    visited[0][0]=1
    while q:
        tmp=q.popleft()
        for i in range(4):
            tmp_y=dy[i]+tmp[0]
            tmp_x=dx[i]+tmp[1]
            if 0<=tmp_x<M and 0<=tmp_y<N:
                if visited[tmp_y][tmp_x]==0 and maze[tmp_y][tmp_x]=='1':
                    q.append([tmp_y,tmp_x])
                    visited[tmp_y][tmp_x]=visited[tmp[0]][tmp[1]]+1
    return visited[N-1][M-1]
N,M=map(int,input().split())
maze=[list(input()) for _ in range(N)]
print(bfs())