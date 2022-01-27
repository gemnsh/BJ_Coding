cnt=int(input())
for i in range(cnt):
    a,b=map(int,input().split(' '))
    sum=1
    for i in range (a):
        sum*=(b-i)
    for i in range (1,a+1):
        sum//=i
    print(int(sum))