from sys import stdin
for _ in range(3):
    num=int(stdin.readline())
    sum=0
    for _ in range(num):
        sum+=int(stdin.readline())
    if sum>0:
        print('+')
    elif sum==0:
        print('0')
    else:
        print('-')