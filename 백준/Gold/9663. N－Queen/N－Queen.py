def check(a):
    for i in range(a):
        if chess_x[i]==chess_x[a] or abs(chess_x[i]-chess_x[a])==a-i:
            return False
    return True        

def queen(n):
    global result
    if n==N:
        result+=1
        return
    for i in range(N):
        chess_x[n]=i
        if check(n):
            queen(n+1)
result=0
N=int(input())
chess_x=[0]*N
queen(0)
print(result)