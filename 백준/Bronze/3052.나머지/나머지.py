num=[]
for i in range(10):
    a=int(input())%42
    num.append(a)
num_1=set(num)
print(len(num_1))