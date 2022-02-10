def gong(a,b):
    if a%b==0:
        return b
    else:
        return gong(b,a%b)

cnt=int(input())
for i in range(cnt):
    A,B=map(int,input().split())
    print(A*B//gong(A,B))