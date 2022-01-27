num=int(input())
for i in range(num):
    x,y=map(int,input().split(' '))
    r=y-x
    n=1
    while 1:
        if r<3:
            print(r)
            break
        elif n%2==0 and n>2: 
            if r<=n/2*((n/2)+1):
                print(n)
                break
        elif n%2==1 and n>2 :
            if r<=((n+1)/2)**2:
                print(n)
                break
        n+=1
