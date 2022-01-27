M, N=map(int,input().split())
num=[]
for i in range(M,N+1):
    check=0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            check=1
            break
    if check==0 and i!=1:
        num.append(i)
for i in num:
    print(i)
