n,m=map(int,input().split())
castle=[[0 for _ in range(m)]for _ in range(n)]
for i in range(n):
    text=input()
    for j in range(len(text)):
        if text[j]=='X':
            castle[i][j]=1
w=set()
h=set()
for i in range(n):
    for j in range(m):
        if castle[i][j]==1:
            w.add(i)
            h.add(j)
print(n-len(w) if n-len(w)>m-len(h) else m-len(h))