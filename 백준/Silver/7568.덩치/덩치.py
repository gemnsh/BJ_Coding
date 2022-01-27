num=int(input())
a=[]
new_list=[]
for i in range(num):
    a.append(list(map(int, input().split())))
for i in range(num):
    cnt=0
    for j in range(num):
        if a[i][0]<a[j][0] and a[i][1]<a[j][1]:
            cnt+=1
    new_list.append(cnt)
for i in range(num):
    print(new_list[i]+1,end=' ')