from collections import deque
T=int(input())
for i in range(T):
    N, M=map(int,input().split())
    d=deque(list(map(int,input().split())))
    index=0
    while 1:
        tmp=d.popleft()
        M-=1
        if d:
            if max(d)<=tmp:
                index+=1
                if M==-1:
                    break
            else:
                d.append(tmp)
                if M<0:
                    M+=(len(d))
        else:
            index+=1
            break
    print(index)