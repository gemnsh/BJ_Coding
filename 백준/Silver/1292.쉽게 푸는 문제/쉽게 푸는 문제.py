input_num=list(map(int,input().split()))
i=0
result=[[0,0],[0,0]]
while 1:
    if input_num[0]<=(i+1)*(i)/2:
        result[0][0]=i
        result[0][1]=1+(i+1)*(i)/2-input_num[0]
        break
    i+=1
j=0
while 1:
    if input_num[1]<=(j+1)*(j)/2:
        result[1][0]=j
        result[1][1]=input_num[1]-(j)*(j-1)/2
        break
    j+=1
if result[1][0]!=result[0][0]:
    answer=result[0][0]*result[0][1]+result[1][0]*result[1][1]
    for k in range(result[0][0]+1,result[1][0]):
        answer+=k*k
    print(int(answer))
else:
    print(int(result[0][0]*(result[1][1]-result[0][0]+result[0][1])))