num=int(input())
list_num=[]
while num>=2:
    for i in range(2,num+1):
        if num%i==0:
            list_num.append(i)
            num=num//i
            break
for i in list_num:
    print(i)