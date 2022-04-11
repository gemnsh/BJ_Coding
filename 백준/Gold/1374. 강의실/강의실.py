import sys
input = sys.stdin.readline
N=int(input())
start=[]
end=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    start.append([tmp[1],tmp[0]])
    end.append([tmp[2],tmp[0]])
start.sort(key=lambda x:x[0],reverse=True)
end.sort(key=lambda x:x[0],reverse=True)
check=[]
result=0
for i in range(end[0][0]+1):
    while start and start[-1][0]<=i : 
        tmp=start.pop()
        check.append(tmp[1])
    while end and i>=end[-1][0]:
        tmp=end.pop()
        check.remove(tmp[1])
    if len(check)>result:
        result=len(check)
print(result)