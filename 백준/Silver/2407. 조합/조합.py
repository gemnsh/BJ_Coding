n,m=map(int,input().split())
result=1
for i in range(max(m,n-m)+1,n+1):
    result*=i
for i in range(1,min(m,n-m)+1):
    result//=i
print(result)