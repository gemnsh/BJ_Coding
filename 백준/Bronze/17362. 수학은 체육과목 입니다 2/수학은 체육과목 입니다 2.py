a=int(input())
a=a%8
result=1
if a==1:
    result=1
elif a==2 or a==0:
    result=2
elif a==3 or a==7:
    result=3
elif a==4 or a==6:
    result=4
elif a==5:
    result=5
print(result)