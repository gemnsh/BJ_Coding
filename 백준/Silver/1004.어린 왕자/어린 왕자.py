count=int(input())
for j in range(count):
    location=list(map(int,input().split()))
    cnt=int(input())
    planet=[]
    start=[]
    dest=[]
    check=0
    for _ in range(cnt):
        planet.append(list(map(int,input().split())))

    for i in range(cnt):
        pass
        start_distance=((location[0]-planet[i][0])**2+(location[1]-planet[i][1])**2)**0.5
        dest_distance=((location[2]-planet[i][0])**2+(location[3]-planet[i][1])**2)**0.5
        if start_distance<planet[i][2]:
            start.append(1)
        elif start_distance>planet[i][2]:
            start.append(0)
        if dest_distance<planet[i][2]:
            dest.append(1)
        elif dest_distance>planet[i][2]:
            dest.append(0)
    for i in range(cnt):
        if start[i]^dest[i]:
            check+=1
    print(check)