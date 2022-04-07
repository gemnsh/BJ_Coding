N=int(input())
house=[list(map(int,input().split())) for _ in range(N)]
visited=[[[0,0,0] for _ in range(N)]for _ in range(N)]
visited[0][1]=[1,0,0]
for i in range(1,2*N-1):
    for j in range(0,i+1):
        if 0<=j<N and 0<=(i-j)<N:
            wall=[1,1,1] # 가세대
            if house[j-1][i-j]==1:
                wall[1]=0
            if house[j][i-1-j]==1:
                wall[0]=0
            if house[j-1][i-1-j]==1:
                wall[2]=0
            if house[j][i-j]==0:
                visited[j][i-j][0]=wall[0]*(visited[j][i-1-j][0]+visited[j][i-1-j][2])+visited[j][i-j][0]
                visited[j][i-j][1]=wall[1]*(visited[j-1][i-j][1]+visited[j-1][i-j][2])+visited[j][i-j][1]
                visited[j][i-j][2]=wall[0]*wall[1]*wall[2]*(visited[j-1][i-1-j][0]+visited[j-1][i-1-j][1]+visited[j-1][i-1-j][2])+visited[j][i-j][2]
print(sum(visited[N-1][N-1]))