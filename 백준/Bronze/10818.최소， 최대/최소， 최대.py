cnt=input()
num=list(map(int,input().split(' ')))
num.sort()
print (f'{num[0]} {num[-1]}')