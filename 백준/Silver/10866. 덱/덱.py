from collections import deque
import sys
que = deque()
N=int(input())
for i in range(N):
    order=list(map(str,sys.stdin.readline().split()))
    if order[0]=='push_back':
        que.append(int(order[1]))
    elif order[0]=='push_front':
        que.appendleft(int(order[1]))
    elif order[0]=='pop_front':
        tmp=-1
        if que:
            tmp=que.popleft()
        print(tmp)
    elif order[0]=='pop_back':
        tmp=-1
        if que:
            tmp=que.pop()
        print(tmp)
    elif order[0]=='size':
        print(len(que))
    elif order[0]=='empty':
        tmp=1
        if que:
            tmp=0
        print(tmp)
    elif order[0]=='front':
        tmp=-1
        if que:
            tmp=que[0]
        print(tmp)
    elif order[0]=='back':
        tmp=-1
        if que:
            tmp=que[-1]
        print(tmp)