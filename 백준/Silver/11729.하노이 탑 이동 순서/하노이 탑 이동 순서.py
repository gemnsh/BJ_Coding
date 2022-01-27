num=int(input())
print((2**num)-1)
def hanoi(n,a,b,c):
    if n==1:
        print(f'{a} {c}')
    else :
        hanoi(n-1,a,c,b)
        print(f'{a} {c}')
        hanoi(n-1,b,a,c)
hanoi(num,1,2,3)