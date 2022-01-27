a,b=input().split()
sum=[]
num=0
if len(a)>len(b):
    b=(len(a)-len(b))*'0'+b
else:
    a=(len(b)-len(a))*'0'+a
a=list(a)
b=list(b)
for i in range(len(a)):
    sum.append(int(a[i])+int(b[i]))
for i in range(len(sum)):
    num+=sum[i]*(10**(len(sum)-i-1))
print(num)