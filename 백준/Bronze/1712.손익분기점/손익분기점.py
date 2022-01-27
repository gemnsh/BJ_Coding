a,b,c=map(int, input().split(' '))
cnt=0
if b>=c:
    cnt= -1
else :
    cnt=int(a /(c-b))+1
print(cnt)