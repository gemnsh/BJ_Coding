dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(start,K):
    q=[start]
    data=0
    while q:
        tmp=q.pop()
        visited [tmp[0]][tmp[1]]=True
        data+=1
        for i in range(4):
            tmp_x=dx[i]+tmp[1]
            tmp_y=dy[i]+tmp[0]
            if 0<=tmp_y<M and 0<=tmp_x<N:
                if visited[tmp_y][tmp_x]==False and b[tmp_y][tmp_x]==K and [tmp_y,tmp_x] not in q:
                    q.append([tmp_y,tmp_x])
    for i in range(M):
        for j in range(N):
            if b[i][j]==K and visited[i][j]==True:
                b[i][j]=''
    return data

N,M=map(int,input().split())
b=[]
result=[0,0] #w,b
visited=[[False for _ in range(N)]for _ in range(M)]
for _ in range(M):
    tmp=input()
    atw=[]
    for k in tmp:
        atw.append(k)
    b.append(atw)
for i in range(M):
    for j in range(N):
        if b[i][j]=='W':
            result[0]+=(dfs([i,j],'W')**2)
        elif b[i][j]=='B':
            result[1]+=(dfs([i,j],'B')**2)
print(*result)