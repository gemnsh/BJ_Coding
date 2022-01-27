cnt=int(input())
for i in range(cnt):
    score_list=list(map(int,input().split()))
    avg=sum(score_list[1:])/score_list[0]
    check=0
    for i in score_list[1:]:
        if avg<i:
            check+=1
    print("%5.3f%%" % ((check/score_list[0])*100))