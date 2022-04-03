from collections import deque
dx=[0,0,-1,1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,-1,1]
def bfs(lst):
    q=deque(lst)
    visited=[[[-1 for _ in range(N)]for _ in range(M)]for _ in range(H)]
    for i in lst:
        visited[i[0]][i[1]][i[2]]=0
    while q:
        tmp=q.popleft()
        for i in range(6):
            tmp_y=dy[i]+tmp[1]
            tmp_x=dx[i]+tmp[2]
            tmp_z=dz[i]+tmp[0]
            if 0<=tmp_y<M and 0<=tmp_x<N and 0<=tmp_z<H:
                if tomato[tmp_z][tmp_y][tmp_x]==0 and visited[tmp_z][tmp_y][tmp_x]<0:
                    visited[tmp_z][tmp_y][tmp_x]=visited[tmp[0]][tmp[1]][tmp[2]]+1
                    tomato[tmp_z][tmp_y][tmp_x]=1
                    q.append([tmp_z,tmp_y,tmp_x])
    tmp_max=0
    count_0=0
    for h in range(H):
        for i in range(M):
            count_0+=tomato[h][i].count(0)
            tmp_max=max(max(visited[h][i]),tmp_max)
    return tmp_max if count_0==0 else -1

N,M,H=map(int,input().split())
tomato=[[list(map(int,input().split())) for _ in range(M)]for _ in range(H)]
c=0
data=[]
for h in range(H):
    for i in range(M):
        for j in range(N):
            if tomato[h][i][j]==1:
                data.append([h,i,j])
    c+=sum(tomato[h][i])

print(bfs(data))  