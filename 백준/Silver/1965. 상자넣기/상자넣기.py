n = int(input())
box=list(map(int,input().split()))
dp=[0]*n
dp[0]=1
for i in range(1,n):
    tmp=0
    for j in range(i):
        if box[i]>box[j]:
            if dp[j]>tmp:
                tmp=dp[j]
    dp[i]=tmp+1
print(max(dp))
