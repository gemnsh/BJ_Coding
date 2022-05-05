import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def find(x,y):
    if x==N-1 and y==M-1:
        dp[y][x]=1
        return dp[y][x]
    elif dp[y][x]!=-1:
        return dp[y][x]
    dp[y][x]=0
    for i in range(4):
        tmpX=x+dx[i]
        tmpY=y+dy[i]
        if 0<=tmpX<N and 0<=tmpY<M:
            if treasure[y][x]>treasure[tmpY][tmpX]:
                dp[y][x]+=find(tmpX,tmpY)
    return dp[y][x]


M, N = map(int, input().split())
treasure = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]

print(find(0, 0))