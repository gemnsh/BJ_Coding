square=list(map(int,input().split()))
num=int(input())
line=[]
garo=[]
sero=[]
area=[]
for i in range(num):
    line.append(list(map(int, input().split())))
line.sort(key=lambda x:(x[0], x[1]))
tmp_g,tmp_s=0,0
for i in range(num):
    if line[i][0]==0:
        square[1]=square[1]-line[i][1]+tmp_g
        garo.append(line[i][1]-tmp_g)
        tmp_g=line[i][1]
    else:
        square[0]=square[0]-line[i][1]+tmp_s
        sero.append(line[i][1]-tmp_s)
        tmp_s=line[i][1]
garo.append(square[1])
sero.append(square[0])
for i in garo:
    for j in sero:
        area.append(i*j)
print(max(area))