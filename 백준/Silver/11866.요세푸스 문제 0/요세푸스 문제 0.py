a,b=map(int,input().split())
cnt=0
lst=list(range(1,a+1))
new_lst=[]
while len(lst)>0:
    cnt=(cnt+b-1)%len(lst)
    new_lst.append(lst[cnt])
    del lst[cnt]
print('<',end='')
for i in range(len(new_lst)-1):
    print(f'{new_lst[i]}, ',end='')
print(f'{new_lst[-1]}>')