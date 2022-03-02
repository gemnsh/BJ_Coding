data=[[0 for _ in range(101)]for _ in range(101)]
max_xy=[0,0]
min_xy=[0,0]
result=0
for _ in range(4):
    a=list(map(int,input().split()))
    for i in range(a[0],a[2]):
        for j in range(a[1],a[3]):
            if data[i][j]==0:
                data[i][j]=1
    if max_xy[0]<a[2]:
        max_xy[0]=a[2]
    if max_xy[1]<a[3]:
        max_xy[1]=a[3]
    if min_xy[0]>a[0]:
        min_xy[0]=a[0]
    if min_xy[1]>a[1]:
        min_xy[1]=a[1]
for i in range(min_xy[0],max_xy[0]+1):
    for j in range(min_xy[1],max_xy[1]+1):
        if data[i][j]==1:
                result+=1
print(result)