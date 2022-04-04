dx=[0,0,1,-1]
dy=[1,-1,0,0]
visited=[]
def dfs(y,x):
    q=[[y,x]]
    a=len(visited)
    if [y,x] not in visited:
        visited.append([y,x])
        while q:
            tmp=q.pop()
            for i in range(4):
                tmp_y=dy[i]+tmp[0]
                tmp_x=dx[i]+tmp[1]
                if 1<=tmp_y<=N and 1<=tmp_x<=M:
                    if [tmp_y,tmp_x] in trash and [tmp_y,tmp_x] not in visited:
                        q.append([tmp_y,tmp_x])
                        visited.append([tmp_y,tmp_x])
    result=len(visited)-a
    return result
answer=0
N,M,K=map(int,input().split())
trash=[list(map(int,input().split()))for _ in range(K)]
for i in range(len(trash)):
    tmp_answer=dfs(trash[i][0],trash[i][1])
    if tmp_answer>answer:
        answer=tmp_answer
print(answer)
