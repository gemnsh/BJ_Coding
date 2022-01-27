N=int(input())
lst=[[0 for _ in range(N)]for _ in range(N)]
check=[[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
def sponge(n,x,y):
    if n==1:
        for i,j in check:
            lst[x+i][y+j]=1
    elif n>1:
        for i,j in check:
            k=n-1
            sponge(k,x+(3**k)*i,y+(3**k)*j)
cnt=0
for i in range(9):
    if 3**i==N:
        cnt=i
        break
sponge(i,0,0)
for i in range (N):
    for j in range (N):
        if lst[j][i]==1:
            print('*', end='')
        else:
            print(' ', end='')
    print()