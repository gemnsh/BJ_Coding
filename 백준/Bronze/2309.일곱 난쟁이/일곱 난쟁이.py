height=[]
height_sum=0
result=[]
for i in range(9):
   height.append(int(input()))
   height_sum+=height[i]
for i in range(8):
   for j in range(i+1,9):
      if height[i]+height[j]+100==height_sum and result==[]: 
         for k in range(9):
            if k!= i and k!=j:
               result.append(height[k])

for i in range(7):
   min_index=i
   for j in range(i+1,7):
      if result[j]<result[min_index]:
         min_index=j
   result[min_index],result[i] = result[i],result[min_index]
for i in range(7):
   print(result[i])