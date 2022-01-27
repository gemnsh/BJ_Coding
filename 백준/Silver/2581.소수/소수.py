M=int(input())
N=int(input())
num=[]
for i in range(M,N+1):
    check=0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            check=1
            break
    if check==0 and i!=1:
        num.append(i)
if len(num)!=0:
    print(sum(num))
    print(num[0])
else:
    print(-1)