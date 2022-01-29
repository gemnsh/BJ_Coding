num=list(map(int,input().split()))
result=0
if num.count(num[0])==3:
    result=10000+1000*num[0]
elif num.count(num[0])==2 :
    result=1000+100*num[0]
elif num.count(num[1])==2 :
    result=1000+100*num[1]
else:
    result=100*max(num)
print(result)