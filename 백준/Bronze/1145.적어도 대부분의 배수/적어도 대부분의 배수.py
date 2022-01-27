n=list(map(int,input().split()))
result=0
check=0
while check<3:
    result+=1
    check=0
    for i in n:
        if result%i==0:
            check+=1
print(result)