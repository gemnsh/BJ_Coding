num=list(map(int,input().split()))
minute=int(input())
num[1]=num[1]+minute
if num[1]>=60:
    num[0]+=num[1]//60
    num[1]=num[1]%60
if num[0]>=24:
    num[0]=num[0]%24
print(f'{num[0]} {num[1]}')