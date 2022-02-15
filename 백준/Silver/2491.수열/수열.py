num_len=int(input())
num_list=list(map(int,input().split()))
max_cnt=0
cnt, cnt_reverse=0,0
for j in range(num_len-1):
   if num_list[j]<=num_list[j+1]:
      cnt+=1
   else:
      cnt=0
   if num_list[j]>=num_list[j+1]:
      cnt_reverse+=1
   else:
      cnt_reverse=0
   if max_cnt<cnt:
      max_cnt=cnt
   if max_cnt<cnt_reverse:
      max_cnt=cnt_reverse
print(max_cnt+1)