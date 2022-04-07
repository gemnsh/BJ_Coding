import sys
input=sys.stdin.readline

N=int(input())
d=[list(map(int,input().split()))for _ in range(N)]
d.append(d[0])
result=0
for i in range(N):
    result+=(d[i][0]*d[i+1][1]-d[i][1]*d[i+1][0])
result=abs(result)*0.5
print(round(result,1))