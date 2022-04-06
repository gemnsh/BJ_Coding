A=input()
B=input()
alpha=[ 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a=[alpha[ord(A[i])-ord('A')] for i in range(len(A))]
b=[alpha[ord(B[i])-ord('A')] for i in range(len(B))]
dp=[]
for i in range(len(A)*2):
    if i%2==0:
        dp.append(a[i//2])
    else:
        dp.append(b[i//2]) 
for i in range(1,2*len(A)-1):
    dp=[(dp[j]+dp[j+1])%10 for j in range(len(dp)-1)]
print(str(dp[0])+str(dp[1]))