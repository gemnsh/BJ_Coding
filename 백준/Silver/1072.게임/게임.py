spider = list(map(int, input().split()))
rate=int(100*spider[1]/spider[0])+1
cnt=int((100*spider[1]-rate*spider[0])/(rate-100)) if rate<100 else -1
spider[0]+=cnt
spider[1]+=cnt
if cnt!=-1:
    while rate>int(100*spider[1]/spider[0]):
        spider[0]+=1
        spider[1]+=1
        cnt+=1
print(cnt)