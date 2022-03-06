import sys
st = []
N=int(input())
for i in range(N):
    order=list(map(str,sys.stdin.readline().split()))
    if order[0]=='push':
        st.append(int(order[1]))
    elif order[0]=='pop':
        tmp=-1
        if st:
            tmp=st.pop()
        print(tmp)
    elif order[0]=='size':
        print(len(st))
    elif order[0]=='empty':
        tmp=1
        if st:
            tmp=0
        print(tmp)
    elif order[0]=='top':
        tmp=-1
        if st:
            tmp=st[-1]
        print(tmp)