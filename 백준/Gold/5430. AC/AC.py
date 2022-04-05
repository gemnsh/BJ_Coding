from collections import deque    
testcase = int(input())
for T in range(1, testcase + 1):
    AC=list(input())
    N=int(input())
    V=deque(list(map(int, ((input().strip('[')).strip(']')).replace(',',' ').split())))
    result = 0
    r_count=0
    for elem in  AC:
        if elem=='R':
            r_count+=1 
        if elem=='D':
            if V:
                if r_count%2==0:
                    V.popleft()
                else:
                    V.pop()
            else:
                result='error'
                break
    V=list(V) 
    if r_count%2==1:
        V.reverse()
    for i in range(len(V)):
        V[i]=str(V[i])
    if result!='error':
        result='['+','.join(V)+']'
    print(f'{result}')