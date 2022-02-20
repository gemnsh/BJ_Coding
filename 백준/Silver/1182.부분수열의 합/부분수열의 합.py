num,s=map(int,input().split())
data_input=list(map(int,input().split()))
result=0
for i in range(1,1<<num):
    tmp=0
    for j in range(num):
        if i&(1<<j):
            tmp+=data_input[j]
    if tmp==s:
        result+=1
print(result)