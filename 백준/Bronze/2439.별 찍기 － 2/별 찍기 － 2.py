count=int(input())
for i in range(count):
    for j in range(count-1-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()