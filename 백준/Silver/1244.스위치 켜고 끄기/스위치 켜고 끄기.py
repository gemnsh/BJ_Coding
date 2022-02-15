switch_num=int(input())
switch_state=list(map(int,input().split()))
std_num=int(input())
for i in range(std_num):
   s,n=map(int,input().split())
   if s==1:
      for k in range(1,switch_num+1):
         if k%n==0 and k>=n:
            switch_state[k-1]=1-switch_state[k-1]
   if s==2:
      j=0
      while n-j>=1 and n-1+j<switch_num:
         if switch_state[n-1-j]==switch_state[n-1+j]:
            j+=1
         else:
            break
      for k in range(n-j,n+j-1):
         switch_state[k]=1-switch_state[k]
while 1:
   if switch_num//20>0:
      tmp=switch_state[:20]
      switch_state=switch_state[20:]
      switch_num-=20
      result=((str(tmp).replace('[','')).replace(']','')).replace(',','')
      print(result)
   else:
      result=((str(switch_state).replace('[','')).replace(']','')).replace(',','')
      print(result)
      break