from collections import deque
dx=[0,-1,0,1]
dy=[1,0,-1,0]
N=int(input())
K=int(input())
apple=[list(map(int,input().split())) for _ in range(K)]
L=int(input())
turn=[list(input().split()) for _ in range(L)]
snake=deque([[1,1]])
direction=3
cnt=0
change_direction=0
while 1:
    tmp=snake.popleft()
    tmp_x=tmp[1]+dx[direction]
    tmp_y=tmp[0]+dy[direction]
    cnt+=1
    if [tmp_y,tmp_x]in snake:
        break
    snake.appendleft(tmp)
    if 1<=tmp_x<N+1 and 1<=tmp_y<N+1:
        if [tmp_y,tmp_x] not in apple:
            snake.pop()
        else:
            apple.remove([tmp_y,tmp_x])
        if change_direction<L:
            if int(turn[change_direction][0])==cnt:
                if turn[change_direction][1]=='D':
                    direction=(direction+1)%4
                    change_direction+=1
                elif turn[change_direction][1]=='L':
                    direction=(direction+3)%4
                    change_direction+=1
        snake.appendleft([tmp_y,tmp_x])
    else:
        break
print(cnt)