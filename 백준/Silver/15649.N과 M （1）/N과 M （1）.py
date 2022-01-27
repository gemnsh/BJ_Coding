n,m = map(int,input().split())

list_num=[]

def ret_num():
    if len(list_num)==m:
        print(' '.join(map(str,list_num)))
        return
    
    for i in range(1,n+1):
        if i not in list_num:
            list_num.append(i)
            ret_num()
            list_num.pop()
            
ret_num()