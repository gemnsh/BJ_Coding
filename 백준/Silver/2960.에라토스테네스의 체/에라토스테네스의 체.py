a,b=map(int,input().split(' '))
num=list(range(2,a+1))
number=0
while len(num):
    number=num[0]
    del num[0]
    b-=1
    if b==0:
        print(number)
    i=0
    while i <len(num):
        if num[i]%number==0:
            b-=1
            if b==0:
                print(num[i])
            del num[i]
            i-=1
        else:
            i+=1