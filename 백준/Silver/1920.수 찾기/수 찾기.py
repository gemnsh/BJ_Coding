num_1=int(input())
a=sorted(list(map(int,input().split())))
num_2=int(input())
b=list(map(int,input().split()))

def bin_check(lst,num,start,end):
    tmp_index=(start+end)//2
    if 0<=start<=end:
        if len(lst)==0:
            return 0
        if lst[tmp_index]<num:
            return bin_check(lst,num,tmp_index+1,end)
        elif lst[tmp_index]==num:
            return 1
        elif lst[tmp_index]>num:
            return bin_check(lst,num,start,tmp_index-1)
    else:
        return 0
        
for i in b:
    print(bin_check(a,i,0,len(a)-1))