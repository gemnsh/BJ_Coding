def per(num, P):
    result = []
    if num == M:
        return [P]
    else:
        for i in range(len(d)):
            if v[i] == True:
                continue
            v[i] = True
            result += per(num+1, P+[d[i]])
            v[i] = False
        return result

N,M=map(int,input().split())
d=list(map(int,input().split()))
v=[False]*N
a=per(0,[])
a.sort()
for i in range(len(a)):
    print(*a[i])