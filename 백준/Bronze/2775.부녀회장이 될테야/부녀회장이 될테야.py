cnt=int(input())
apt = [[0 for _ in range(15)] for _ in range(15)]
for i in range(0,15):
    for j in range(1,15):
        if i==0:
            apt[i][j]=j
        else:
            for k in range(j+1):
                apt[i][j]+=apt[i-1][k]
for i in range(cnt):
    a=int(input())
    b=int(input())
    print(apt[a][b])
