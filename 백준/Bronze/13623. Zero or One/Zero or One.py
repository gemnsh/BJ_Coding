A,B,C=map(int,input().split())
d={0:[],1:[]}
if A==0:
    d[0].append('A')
else:
    d[1].append('A')
if B==0:
    d[0].append('B')
else:
    d[1].append('B')
if C==0:
    d[0].append('C')
else:
    d[1].append('C')
if len(d[0])==1:
    print(d[0][0])
elif len(d[1])==1:
    print(d[1][0])
if len(d[0])*len(d[1])==0:
    print('*')