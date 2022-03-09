C,R=map(int,input().split())
K= int(input())
a=[[0 for _ in range(C)] for _ in range(R)]
i,d=1,0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
tmp_x,tmp_y=0,0
chk=False
while 1:
    if K>C*R:
        print(0)
        break
    a[tmp_y][tmp_x]=i
    if K==i:
        print(tmp_x+1,tmp_y+1)
        break
    if not(0<=tmp_x+dx[d]<C) or not(0<=tmp_y+dy[d]<R):
        chk=True
    if 0<=tmp_x+dx[d]<C and 0<=tmp_y+dy[d]<R:
        if a[tmp_y+dy[d]][tmp_x+dx[d]]!=0:
            chk=True
    if chk:
        chk=False
        d=(d+1)%4
    i+=1
    tmp_x=tmp_x+dx[d]
    tmp_y=tmp_y+dy[d]