import sys
input = sys.stdin.readline
num=int(input())
cnt=[0 for _ in range(10001)]
for _ in range(num):
    a=int(input())
    cnt[a]+=1
for i in range(10001):
    while cnt[i]:
        print(i)
        cnt[i]-=1