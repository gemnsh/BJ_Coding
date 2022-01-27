cnt= int(input())
score=list(map(int,input().split()))
score.sort()
print((sum(score)/cnt)*(100/score[-1]))