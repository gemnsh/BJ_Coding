import re
num=int(input())
for _ in range(num):
    data=input()
    a=re.compile('(100+1+|01)+')
    result = a.fullmatch(data)
    if result:
        print('YES')
    else:
        print('NO')