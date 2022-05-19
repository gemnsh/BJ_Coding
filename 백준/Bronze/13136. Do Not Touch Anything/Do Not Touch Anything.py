a,b,c=map(int,input().split())
d=a//c if a%c==0 else (a//c)+1
e=b//c if b%c==0 else (b//c)+1
print(d*e)