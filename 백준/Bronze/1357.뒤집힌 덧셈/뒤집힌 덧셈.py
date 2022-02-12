def rev(s):
    tmp=''
    for i in range(len(s)-1,-1,-1):
        tmp+=s[i]
    return int(tmp)
a,b=input().split()

print(rev(str(rev(a)+rev(b))))