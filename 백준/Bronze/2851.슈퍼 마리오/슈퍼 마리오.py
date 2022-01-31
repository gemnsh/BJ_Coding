mush=[]
for _ in range(10):
    mush.append(int(input()))
score=0
for i in mush:
    if score+i<=100:
        score+=i
        continue
    else:
        if score+i-100<=100-score:
            score+=i
            break
        else:
            break
print(score)