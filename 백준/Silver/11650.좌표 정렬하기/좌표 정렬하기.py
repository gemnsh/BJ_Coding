count=int(input())
location=[]
for _ in range(count):
    location.append(list(map(int,input().split())))
location=sorted(location,key=lambda x:(x[0],x[1]))
for i in location:
    print(f'{i[0]} {i[1]}')