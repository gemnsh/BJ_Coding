n=int(input())
dp=[50000]*(n+1)
dp[0],dp[1]=0,1
for i in range(n+1):
    check=1
    a=check**2
    while a<=i:
        dp[i]=min(dp[i],dp[i-a]+1)
        check+=1
        a+=(2*check-1)
print(dp[n])