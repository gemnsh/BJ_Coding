num=(int(input())//100)*100
div_num=int(input())
i=0
while 1:
    if (num+i)%div_num==0:
        break
    else:
        i+=1
print(f'{i:02d}')