num=[]
for i in range(9):
    a=int(input())
    num.append(a)
b=num.copy()
b.sort()
for i in range(9):
    if b[-1]==num[i]:
        print(b[-1])
        print(i+1)