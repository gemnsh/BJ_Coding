n,m=map(int,input().split())
data=[list(map(int,input().split()))for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
visited=[[0 for _ in range(m)]for _ in range(n)]
def fs(y,x):
    q=[[y,x]]
    visited[y][x]=1
    check=1
    while q:
        tmp=q.pop()
        for i in range(4):
            tmp_x=tmp[1]+dx[i]
            tmp_y=tmp[0]+dy[i]
            if 0<=tmp_x<m and 0<=tmp_y<n:
                if visited[tmp_y][tmp_x]==0 and data[tmp_y][tmp_x]==1:
                    visited[tmp_y][tmp_x]=1
                    q.append([tmp_y,tmp_x])
                    check+=1
    return check
result=0
counting=0
for i in range(n):
    for j in range(m):
        if data[i][j]==1 and visited[i][j]==0:
            tmp_result=fs(i,j)
            if tmp_result>result:
                result=tmp_result
            counting+=1
print(counting)
print(result)