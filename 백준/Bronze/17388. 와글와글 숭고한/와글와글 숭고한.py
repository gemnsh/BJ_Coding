a,b,c=map(int,input().split())
m=min(a,b,c)
result='OK'
if a+b+c<100:
    if a==m:
        result='Soongsil'
    elif b==m:
        result='Korea'
    else:
        result='Hanyang'
print(result)
