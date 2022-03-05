from collections import deque
N=int(input())
queue = deque(list(range(1,N+1)))
i=0
while len(queue)>1:
    tmp=queue.popleft()
    if i%2==1:
        queue.append(tmp)
    i+=1
print(queue[0])