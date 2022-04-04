def bfs(a):
    q=[a]
    visited=[]
    while q:
        tmp=q.pop(0)
        if tmp not in visited:
            visited.append(tmp)
            tmp_v=[]
            for i in V:
                if (i[0] not in visited or i[0] not in tmp_v) and i[1]==tmp:
                    tmp_v.append(i[0])
                elif(i[1] not in visited or i[1] not in tmp_v) and i[0]==tmp:
                    tmp_v.append(i[1])
            tmp_v.sort()
            q.extend(tmp_v)
    return visited
def dfs(a):
    q=[a]
    visited=[]
    while q:
        tmp=q.pop()
        if tmp not in visited:
            visited.append(tmp)
            tmp_v=[]
            for i in V:
                if (i[0] not in visited or i[0] not in tmp_v) and i[1]==tmp:
                    tmp_v.append(i[0])
                elif(i[1] not in visited or i[1] not in tmp_v) and i[0]==tmp:
                    tmp_v.append(i[1])
            tmp_v.sort(reverse=True)
            q.extend(tmp_v)
    return visited

n,m,v=map(int,input().split())
V=[list(map(int,input().split())) for _ in range(m)]
print(*dfs(v))
print(*bfs(v))