N=int(input())
data=[0]*(N+1)
for i in range(2,N+1):
    if i%3==0 and i%2==0:
        data[i]=min(data[i-1],data[i//3],data[i//2])+1
    elif i%3==0:
        data[i]=min(data[i-1],data[i//3])+1
    elif i%2==0:
        data[i]=min(data[i-1],data[i//2])+1
    else:
        data[i]=data[i-1]+1
print(data[N])