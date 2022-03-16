N=int(input())
d=[]
for i in range(N):
    d.append(list(map(int,input().split())))
que=[[0,0]]
dx=[1,0]
dy=[0,1]
visited=[]
result=0
while que:
    tmp=que.pop()
    if d[tmp[0]][tmp[1]]==-1:
        result=1
        break
    if tmp not in visited:
        visited.append([tmp[0],tmp[1]])
        for i in range(2):
            t_x=d[tmp[0]][tmp[1]]*dx[i]+tmp[1]
            t_y = d[tmp[0]][tmp[1]] * dy[i] + tmp[0]
            if 0<=t_x<N and 0<=t_y<N:
                que.append([t_y,t_x])
print('HaruHaru'if result==1 else 'Hing')