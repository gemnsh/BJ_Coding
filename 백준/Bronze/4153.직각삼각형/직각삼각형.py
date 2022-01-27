tri=[]
tri.append(list(map(int,input().split())))
while tri[-1]!=[0,0,0]:
    a=sorted(tri[-1])
    if a[2]**2==a[0]**2+a[1]**2:
        print('right')
    else:
        print('wrong')
    tri.append(list(map(int,input().split())))