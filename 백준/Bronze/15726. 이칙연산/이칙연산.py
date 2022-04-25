A,B,C=map(int,input().split())
t=int(A*B/C)
u=int(A/B*C)
print(max(t,u))