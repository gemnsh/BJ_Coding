w,h=map(int, input().split())
p,q=map(int, input().split())
t=int(input())
now=[(p+t)%(2*w),(q+t)%(2*h)]
d=[1,1]
if now[0]>w:
    now[0]=2*w-now[0]
if now[1]>h:
    now[1]=2*h-now[1]
print(*now)
