import sys
input=sys.stdin.readline

def cutting(n,y,x):
    global result
    a,b=check(n,y,x)
    if a:
        result[data[y][x]]+=1
        return
    if n==3:
        result[-1]+=b[0]
        result[0]+=b[1]
        result[1]+=b[2]
        return
    else:
        cutting(n//3,y,x)
        cutting(n//3,y,x+n//3)
        cutting(n//3,y,x+ 2*n//3)
        cutting(n//3,y+n//3,x)
        cutting(n//3,y+n//3,x+n//3)
        cutting(n//3,y+n//3,x+2*n//3)
        cutting(n//3,y+2*n//3,x)
        cutting(n//3,y+2*n//3,x+n//3)
        cutting(n//3,y+2*n//3,x+2*n//3)
  
def check(n,y,x):
    count=[0,0,0]
    res=True
    for i in range(n):
            for j in range(n):
                if data[y+i][x+j]==-1:
                    count[0]+=1
                elif data[y+i][x+j]==0:
                    count[1]+=1
                elif data[y+i][x+j]==1:
                    count[2]+=1
                if count[0]*count[1]>0 or count[0]*count[2]>0 or count[1]*count[2]>0:
                    res=False
    return res,count

N=int(input())
data=[list(map(int,input().split())) for _ in range(N)]
result={-1:0,0:0,1:0}
cutting(N,0,0)
print(result[-1])
print(result[0])
print(result[1])