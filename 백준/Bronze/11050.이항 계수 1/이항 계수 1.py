a,b=map(int,input().split())
def binominal(n,k):
    if k==0 or n==k:
        return 1
    elif n>=1 and k>=1:
        return binominal(n-1,k-1)+binominal(n-1,k)
print(binominal(a,b))