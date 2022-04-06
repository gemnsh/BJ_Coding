import sys
input = sys.stdin.readline
print = sys.stdout.write
N,M = map(int,input().split())
D={}
for _ in range(N):
    tmp = list(input().strip().split())
    D[tmp[0]]=tmp[1]
for _ in range(M):
    tmp = input().strip()
    print("%s\n" % D[tmp])