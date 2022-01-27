sq=[]
x=[]
y=[]
a=[0,0]
for i in range(3):
    sq.append(list(map(int,input().split())))
for i in range(3):
    x.append(sq[i][0])
    y.append(sq[i][1])
if x[0]==x[1]:
    a[0]=x[2]
elif x[1]==x[2]:
    a[0]=x[0]
elif x[0]==x[2]:
    a[0]=x[1]
if y[0]==y[1]:
    a[1]=y[2]
elif y[1]==y[2]:
    a[1]=y[0]
elif y[0]==y[2]:
    a[1]=y[1]

print(f'{a[0]} {a[1]}')