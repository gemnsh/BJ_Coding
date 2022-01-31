num=list(map(int,input().split()))
time=int(input())
time=time+num[0]*3600+num[1]*60+num[2]
time_list=[]
time_list.append((time//3600)%24)
time_list.append((time%3600)//60)
time_list.append((time%3600)%60)
print(f'{time_list[0]} {time_list[1]} {time_list[2]}')