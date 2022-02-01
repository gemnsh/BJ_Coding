num=int(input())
score=[]
check=0
for _ in range(num):
    score.append(int(input()))
for i in range(len(score)-1,0,-1):
    while score[i]<=score[i-1]:
        score[i-1]-=1
        check+=1
print(check)