def check(a,b):
    c=a%b
    if c==0:
        return b
    else:
        e=check(b,c)
    return e
num = list(map(int, input().split()))
result=check(num[0],num[1])
print(result)
print(num[0]*num[1]//result)