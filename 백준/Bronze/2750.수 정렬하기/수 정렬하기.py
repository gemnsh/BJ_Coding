num=int(input())
array_num=[]
for _ in range(num):
    array_num.append(int(input()))
for i in range(num):
    for j in range(num-i-1):
        if array_num[j]>array_num[j+1]:
            tmp=array_num[j]
            array_num[j]=array_num[j+1]
            array_num[j+1]=tmp
for i in range(num):
    print(array_num[i])