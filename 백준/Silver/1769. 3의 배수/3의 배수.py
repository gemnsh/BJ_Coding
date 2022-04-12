def deep(n,count):
    global result
    if len(n)==1:
        result[0]=count
        if int(n)%3==0:
            result[1]='YES'
        return
    else:
        s=0
        for i in n:
            s+=int(i)
        deep(str(s),count+1)
N=input()
result=[0,'NO']
deep(N,0)
print(result[0])
print(result[1])