num=int(input())
check=1
sum=0
bun_ja=1
bun_mo=1
while 1:
    if sum<num<=sum+check:
        if check%2==0:
            bun_mo=check-(num-sum)+1
            bun_ja=num-sum
        else :
            bun_ja=check-(num-sum)+1
            bun_mo=num-sum
        print(f'{bun_ja}/{bun_mo}')
        break
    sum+=check
    check+=1
