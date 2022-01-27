num=int(input())
a=[]
for i in range(num):
    a.append(input())
a.sort()
a=sorted(a,key=lambda x: len(x))
tmp=''
for i in range(num):
    if tmp !=a[i]:
        print(a[i])
        tmp=a[i]