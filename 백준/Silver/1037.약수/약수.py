num=int(input())
yakksu=list(map(int,input().split()))
yakksu.sort()
if num==1:
    print(yakksu[0]**2)
else:
    print(yakksu[0]*yakksu[-1])