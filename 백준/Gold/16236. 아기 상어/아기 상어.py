from collections import deque
dx=[0,-1,1,0]
dy=[-1,0,0,1]

def bfs(e):
    q=deque([e[0]])
    visited=[[0 for _ in range(N)]for _ in range(N)]
    visited[e[0][0]][e[0][1]]=0
    check_order=[]
    while q:
        tmp=q.popleft()
        for i in range(4):
            tmp_x=tmp[1]+dx[i]
            tmp_y=tmp[0]+dy[i]
            if 0<=tmp_x<N and 0<=tmp_y<N:
                if visited[tmp_y][tmp_x]==0 and (fish[tmp_y][tmp_x]==e[1] or fish[tmp_y][tmp_x]==0 ):
                    q.append([tmp_y,tmp_x])
                    visited[tmp_y][tmp_x]=1+visited[tmp[0]][tmp[1]]
                if 0<fish[tmp_y][tmp_x]<e[1]:
                    if visited[tmp_y][tmp_x]==0:
                        check_order.append([tmp_y,tmp_x,1+visited[tmp[0]][tmp[1]]])
                        q.append([tmp_y,tmp_x])
                        visited[tmp_y][tmp_x]=1+visited[tmp[0]][tmp[1]]
    if check_order:
        check_order.sort(key=lambda x:(x[2],x[0],x[1]))
        return [check_order[0][:],visited[check_order[0][0]][check_order[0][1]]]
    return -1
N=int(input())
fish=[list(map(int,input().split()))for _ in range(N)]
fish_size=[[]for _ in range(7)]
start=[[0,0],2]
for i in range(N):
    for j in range(N):
        for k in (1,2,3,4,5,6,9):
            if fish[i][j]==9:
                start[0]=[i,j]
            elif fish[i][j]==k:
                fish_size[k].append([i,j])
eat_sum=0
check=False
for i in range(2,8):
    start[1]=i
    eat_count=0
    while eat_count<i<=6 and not check:
        a=bfs(start)
        if a!=-1:
            fish[start[0][0]][start[0][1]]=0
            start[0]=a[0][:]
            eat_count+=1
            eat_sum+=a[1]
            fish[a[0][0]][a[0][1]]=9
            
        else:
            check=True
    if i==7:
        while not check:
            a=bfs(start)
            if a!=-1:
                fish[start[0][0]][start[0][1]]=0
                start[0]=a[0][:]
                eat_count+=1
                eat_sum+=a[1]
                fish[a[0][0]][a[0][1]]=9
            else:
                check=True
    if check:
        break
print(eat_sum)
