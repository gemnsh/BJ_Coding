count=int(input())
for i in range(count):
    x,y=map(int,input().split(' '))
    print(f'Case #{i+1}: {x+y}')