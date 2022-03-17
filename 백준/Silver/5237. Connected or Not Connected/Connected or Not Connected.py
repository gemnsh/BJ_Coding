t=int(input())
for test in range(1,t+1):
    d=list(map(int,input().split()))
    a=[[] for _ in range(d[0])]
    for i in range(d[1]):
        a[d[2*i+2]].append(d[2*i+3])
        a[d[2*i+3]].append(d[2 * i + 2])

    visited=[]
    q=[d[2]]
    while q:
        tmp=q.pop()
        if tmp not in visited:
            visited.append(tmp)
            q.extend(a[tmp])
    print("Connected." if len(visited)==d[0] else "Not connected.")