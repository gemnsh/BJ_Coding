e = [True] * 1000000
for i in range(2, 1001):
    if e[i]:
        for j in range(i + i, 1000000, i):
            e[j] = False
while 1:
    n=int(input())
    if n==0:
        break
    check=0
    a=n-3
    while check==0:
        if e[a]==True and e[n-a]==True and check==0:
            print(f'{n} = {n-a} + {a}' )
            check=1
        a-=1