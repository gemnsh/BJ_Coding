def bfs(a):
    q=[a]
    visited=[-1]*(n+1)
    visited[a]=0
    while q:
        tmp=q.pop(0)
        for i in V:
            if visited[i[0]]==-1 and i[1]==tmp:
                q.append(i[0])
                visited[i[0]]=visited[i[1]]+1

            elif visited[i[1]]==-1 and i[0]==tmp:
                q.append(i[1])
                visited[i[1]]=visited[i[0]]+1
    return sum(visited)

n,m=map(int,input().split())
V=[list(map(int,input().split())) for _ in range(m)]
result=[50000000000,0]
for i in range(1,n+1):
    bfs_i=bfs(i)
    if result[0]>bfs_i:
        result[0]=bfs_i
        result[1]=i
print(result[1])