room=int(input())
check=0
cnt=0
while check==0:
    min_room=(cnt*(cnt+1)/2)*6+1
    max_room=((cnt+1)*(cnt+2)/2)*6+1
    if room==1:
        check=1
    elif min_room<room<=max_room:
        check=cnt+2
    cnt+=1
print(check)