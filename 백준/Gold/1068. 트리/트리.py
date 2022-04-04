def dfs(n):
    q=[n]
    visited=[n]
    while q:
        tmp=q.pop()
        for i in range(N):
            if tree[i]==tmp:
                visited.append(i)
                q.append(i)
    return visited
N=int(input())
tree=list(map(int,input().split()))
L=int(input())
v=dfs(L)
check=[]
for i in range(N):
    if i in v:
        tree[i]=-4
a=tree[:]
result=0
for i in range(N):
    if i in a:
        tree[i]=-4
    if tree[i]!= -4:
        result+=1
print(result)