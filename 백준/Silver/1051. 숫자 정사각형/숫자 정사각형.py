N,M=map(int,input().split())
sq=[input() for _ in range(N)]
start=min(M,N)
check=True
result=0
for k in range(start,0,-1):
    if check:
        for i in range(N-k+1):
            if check:
                for j in range(M-k+1):
                    if sq[i][j]==sq[i+k-1][j+k-1] and sq[i][j]==sq[i+k-1][j] and sq[i][j]==sq[i][j+k-1]:
                        check=False
                        result=k*k
print(result)