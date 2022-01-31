num=input()
result=''
value=len(num)
for i in range(value):
    new=''
    a=str(int(num[i])//4)
    b=str((int(num[i])%4)//2)
    c=str(int(num[i])%2)
    new=a+b+c
    if i==0:
        if a=='0' and b=='0':
            print(c,end='')
        elif a=='0':
            print(b+c,end='')
        else:
            print(new,end='')    
    else: 
        print(new,end='')
