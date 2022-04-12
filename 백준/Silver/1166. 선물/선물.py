def b_check(start,end):
    tmp=0
    for k in range(10000):
        tmp=(start+end)/2
        if (L//tmp)*(W//tmp)*(H//tmp)>=N:
            start=tmp
        else:
            end=tmp
    return tmp
N,L,W,H=map(int,input().split())
print(b_check(0,max(L,W,H)))