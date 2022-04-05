def rec(n,y,x,a):
    if n==1:
        z[0][0]=a
        z[0][1]=a+1
        z[1][0]=a+2
        z[1][1]=a+3
        return
    tmp=(2**(2*n-2))
    new_y=y+2**(n-1)
    new_x=x+2**(n-1)
    if y<=r<new_y and x<=c<new_x:
        rec(n-1,y,x,a)
    elif y<=r<new_y and new_x<=c:
        rec(n-1,y,new_x,a+tmp)
    elif new_y<=r and x<=c<new_x:
        rec(n-1,new_y,x,a+2*tmp)
    else:
        rec(n-1,new_y,new_x,a+3*tmp)
N,r,c=map(int,input().split())
z=[[0,0],[0,0]]
rec(N,0,0,0)
print(z[r%2][c%2])