n=input()
result=0
for i in range(1,len(n)):
    if result==1:
        break
    t_1=n[:i]
    t_2=n[i:]
    check=[1,1]
    for j in range(i):
        check[0]*=int(t_1[j])
    for j in range(len(t_2)):
        check[1]*=int(t_2[j])
    if check[0]==check[1]:
        result=1
print('YES'if result==1 else 'NO')