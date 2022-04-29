n,w,h,l=map(int,input().split())
result=(w//l)*(h//l)

if result>n:
    print(n)
else:
    print(result)