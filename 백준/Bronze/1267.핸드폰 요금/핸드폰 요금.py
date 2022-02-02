num=int(input())
Y,M=0,0
phone=list(map(int,input().split()))
for i in range(num):
    Y+=10*(int(phone[i]/30)+1)
    M+=15*(int(phone[i]/60)+1)
if Y<M:
    print(f'Y {Y}')
elif Y==M:
    print(f'Y M {Y}')
else:
    print(f'M {M}')