num=int(input())
while num!=0:
    tmp=[]
    check=True
    while num>=10:
        tmp.append(num%10)
        num=num//10
    tmp.append(num)
    for i in range(int(len(tmp)/2)):
        if tmp[i]!=tmp[-i-1]:
            check=False
    if check:
        print('yes')
    else:
        print('no')
    num=int(input())