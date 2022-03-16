T=int(input())
for test in range(1,T+1):
    M,N,K=map(int,input().split())
    d=[]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    visited=[]
    for i in range(K):
        d.append(tuple(map(int,input().split())))
    result=0
    while d:
        a=d[0]
        s = [a]
        while s:
            tmp=s.pop()
            if [tmp[0],tmp[1]] not in visited:
                visited.append(tmp)
                for i in range(4):
                    if (tmp[0]+dy[i],tmp[1]+dx[i]) not in visited and (tmp[0]+dy[i],tmp[1]+dx[i]) in d:
                        s.append((tmp[0]+dy[i],tmp[1]+dx[i]))
        d=list(set(d)-set(visited))
        result+=1
    print(f'{result}')