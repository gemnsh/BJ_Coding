cnt=int(input())
num=int(input())
lst = [[0 for _ in range(cnt+2)] for _ in range(cnt+2)]
direction=[[0,1],[1,0],[0,-1],[-1,0]]
value=cnt**2
drc=0
now_x,now_y=1,1
loc=[0,0]
while value>0:
    lst[now_y][now_x]=value
    if value==num:
        loc=[now_x,now_y]
    if lst[now_y+direction[drc][1]][now_x+direction[drc][0]]!=0 or now_x+direction[drc][0]<1 or now_x+direction[drc][0]>=cnt+1 or now_y+direction[drc][1]<1 or now_y+direction[drc][1]>=cnt+1:
        drc=(drc+1)%4
    now_x+=direction[drc][0]
    now_y+=direction[drc][1]
    value-=1

for i in range(1,cnt+1): 
    for j in range(1,cnt+1): 
        print(lst[i][j] , end = ' ')
    print()
print(f'{loc[1]} {loc[0]}')