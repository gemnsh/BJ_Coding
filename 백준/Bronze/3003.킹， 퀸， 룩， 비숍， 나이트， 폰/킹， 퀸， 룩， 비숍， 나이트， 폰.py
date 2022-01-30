lst=[1,1,2,2,2,8]
input_chess=list(map(int,input().split()))
result=[0,0,0,0,0,0]
for i in range(6):
    result[i]=lst[i]-input_chess[i]
print(f'{result[0]} {result[1]} {result[2]} {result[3]} {result[4]} {result[5]} ')