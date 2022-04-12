dx=[0,0,-1,1]
dy=[1,-1,0,0]
R,C,K=map(int,input().split())
visited=[[True for _ in range(C)]for _ in range(R)]
visited[R-1][0]=False
result=0
def dfs(y,x,k):
    global result
    if k==K:
        if y==0 and x==C-1:
            result+=1
        return
    else:
        for i in range(4):
            tmp_y=y+dy[i]
            tmp_x=x+dx[i]
            if 0<=tmp_y<R and 0<=tmp_x<C:
                if visited[tmp_y][tmp_x] and maze[tmp_y][tmp_x]=='.':
                    k+=1
                    visited[tmp_y][tmp_x]=False
                    dfs(tmp_y,tmp_x,k)
                    visited[tmp_y][tmp_x]=True
                    k-=1
                    
maze=[input() for _ in range(R) ]
dfs(R-1,0,1)
print(result)