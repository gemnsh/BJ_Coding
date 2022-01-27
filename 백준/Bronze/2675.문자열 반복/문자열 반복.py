cnt= int(input())
for i in range(cnt):
    a=list(map(str,input().split()))
    new_str=''
    for j in a[1]:
        new_str+=int(a[0])*j
    print(new_str)