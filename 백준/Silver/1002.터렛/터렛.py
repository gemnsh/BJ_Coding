num=int(input())
for i in range(num):
    x_1,y_1,r_1,x_2,y_2,r_2=map(int,input().split(' '))
    answer=0
    loc=((x_2-x_1)**2+(y_2-y_1)**2)**0.5
    a=((r_1 - r_2)**2)**0.5
    if loc==0 and r_1 ==r_2:
        answer=-1
    elif a<loc<r_1+r_2:
        answer=2
    elif loc==r_1+r_2 or a==loc:
        answer=1
    elif loc>r_1+r_2 or loc<a:
        answer=0
    print(answer)