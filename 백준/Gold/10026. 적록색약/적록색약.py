dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(y,x,color):
    q=[[y,x]]
    visited=[]
    while q:
        tmp=q.pop()
        visited.append([tmp[0],tmp[1]])
        for i in range(4):
            tmp_y=dy[i]+tmp[0]
            tmp_x=dx[i]+tmp[1]
            if 0<=tmp_x<N and 0<=tmp_y<N:
                if rgb[tmp_y][tmp_x]==color and [tmp_y,tmp_x] not in visited:
                    q.append([tmp_y,tmp_x])
    for elem in visited:
        rgb[elem[0]][elem[1]]=False
def dfs2(y,x,color):
    q=[[y,x]]
    visited=[]
    while q:
        tmp=q.pop()
        visited.append([tmp[0],tmp[1]])
        for i in range(4):
            tmp_y=dy[i]+tmp[0]
            tmp_x=dx[i]+tmp[1]
            if 0<=tmp_x<N and 0<=tmp_y<N:
                if color=='B':
                    if rgb2[tmp_y][tmp_x]==color and [tmp_y,tmp_x] not in visited:
                        q.append([tmp_y,tmp_x])
                else:
                    if (rgb2[tmp_y][tmp_x]=='G' or rgb2[tmp_y][tmp_x]=='R')  and [tmp_y,tmp_x] not in visited:
                        q.append([tmp_y,tmp_x])
    for elem in visited:
        rgb2[elem[0]][elem[1]]=False

N=int(input())
rgb=[list(input()) for _ in range(N)]
rgb2=[]
result=[0,0]
for i in range(N):
    rgb2.append(rgb[i][:])
for i in range(N):
    for j in range(N):
        if rgb[i][j]:
            dfs(i,j,rgb[i][j])
            result[0]+=1
        if rgb2[i][j]:
            dfs2(i,j,rgb2[i][j])
            result[1]+=1
print(*result)