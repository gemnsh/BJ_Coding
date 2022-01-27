a=int(input())

def fib2(n):
    b=[1,0]
    if n>=2:
        for i in range(2,n+1):
            b.append(b[i-2]+b[i-1])
    return b[n]
for i in range(a):
    num=int(input())
    c,d= fib2(num),fib2(num+1)
    print(f'{c} {d}')