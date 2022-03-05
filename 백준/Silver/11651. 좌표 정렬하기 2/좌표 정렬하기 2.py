n=int(input())
coord = [list(map(int, input().split())) for _ in range(n)]
coord.sort(key= lambda x : (x[1],x[0]))
for i in range(n):
    print(*coord[i])