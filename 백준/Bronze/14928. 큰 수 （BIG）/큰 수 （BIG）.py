N=input()
a=[]
for i in range(len(N)//10):
    a.append(N[10*i:10*(i+1)])
a.append(N[10*(len(N)//10):])
result=str(int(a[0])%20000303)
for i in range(len(a)-1):
    result=str(int(result+a[i+1])%20000303)
print(result)