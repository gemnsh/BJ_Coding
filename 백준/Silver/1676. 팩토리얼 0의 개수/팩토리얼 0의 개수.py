N=int(input())
k=5
result=0
while k<=N:
    result+=N//k
    k*=5
print(result)