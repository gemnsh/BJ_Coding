def tri(x, y, n):
    if n == 3:
        ans[x][y] = '*'
        ans[x+1][y-1] = ans[x+1][y+1] = '*'
        for i in range(-2, 3):
            ans[x+2][y+i] = '*'
    else:
        m = n // 2
        tri(x, y, m)
        tri(x+m, y-m, m)
        tri(x+m, y+m, m)


N = int(input())
ans = [[' '] * 2 * N for _ in range(N)]

tri(0, N-1, N)
for row in ans:
    print("".join(row))