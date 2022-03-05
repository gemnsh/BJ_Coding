import sys
n, m, b = map(int, sys.stdin.readline().split())
mine = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height=256
result=[sys.maxsize,0]
while height>=0:
    max,min=0,0
    for i in range(n):
        for j in range(m):
            if mine[i][j]<height:
                min+=(height-mine[i][j])
            else:
                max+=(mine[i][j]-height)
    item=max+b
    if item<min:
        height-=1
        continue
    time=2*max+min
    if time<result[0]:
        result[0]=time
        result[1]=height
    height-=1
print(*result)