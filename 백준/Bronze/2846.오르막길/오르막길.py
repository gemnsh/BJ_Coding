num=int(input())
h_list=list(map(int,input().split()))
max=0
least_height=0
check=False
for i in range(len(h_list)-1):
    if h_list[i]<h_list[i+1] and check==False:
        check=True
        least_height=h_list[i]
    if  h_list[i]<h_list[i+1] and check==True:
        now=h_list[i+1]-least_height
        if now>max:
            max=now
    if h_list[i]>=h_list[i+1]:
        least_height=0
        check=False
print(max)