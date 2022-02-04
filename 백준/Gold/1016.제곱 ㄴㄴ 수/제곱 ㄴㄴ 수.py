import math
min_max=list(map(int,input().split()))
num_stack=[True for _ in range(min_max[1]-min_max[0]+1)]
i=2
while i**2<=min_max[1]:
    tmp=math.ceil(min_max[0]/(i**2))
    while tmp*(i**2)<=min_max[1] :
        if tmp>0:
            num_stack[tmp*(i**2)-min_max[1]-1]=False
        tmp+=1
    i+=1
print(sum(num_stack))