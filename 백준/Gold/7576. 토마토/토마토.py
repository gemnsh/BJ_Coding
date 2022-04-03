from collections import deque
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(lst):
    q=deque(lst)
    visited=[[-1 for _ in range(N)]for _ in range(M)]
    for i in lst:
        visited[i[0]][i[1]]=0
    while q:
        tmp=q.popleft()
        for i in range(4):
            tmp_y=dy[i]+tmp[0]
            tmp_x=dx[i]+tmp[1]
            if 0<=tmp_y<M and 0<=tmp_x<N:
                if tomato[tmp_y][tmp_x]==0 and visited[tmp_y][tmp_x]<0:
                    visited[tmp_y][tmp_x]=visited[tmp[0]][tmp[1]]+1
                    tomato[tmp_y][tmp_x]=1
                    q.append([tmp_y,tmp_x])
    tmp_max=0
    count_0=0
    for i in range(M):
        count_0+=tomato[i].count(0)
        tmp_max=max(max(visited[i]),tmp_max)
    return tmp_max if count_0==0 else -1

N,M=map(int,input().split())
tomato=[list(map(int,input().split())) for _ in range(M)]
c=0
data=[]
for i in range(M):
    for j in range(N):
        if tomato[i][j]==1:
            data.append([i,j])
    c+=sum(tomato[i])

print(bfs(data))  