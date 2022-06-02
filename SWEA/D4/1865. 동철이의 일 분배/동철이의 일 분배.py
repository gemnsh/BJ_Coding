def calc(now_per,now_work,n):
    global max_per
    if now_work==n:
        if max_per<now_per:
            max_per=now_per
        return
    if now_per<=max_per:
        return
    for i in range(n):
        if visited[i]==1:
            visited[i]=0
            calc(now_per*per[now_work][i]/100,now_work+1,n)  
            visited[i]=1
T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    per=[list(map(int,input().split())) for _ in range(N)]
    global max_per
    max_per=0
    visited=[1 for _ in range(N)]
    calc(1,0,N)
    print(f'#{test_case} {max_per*100:0.6f}')