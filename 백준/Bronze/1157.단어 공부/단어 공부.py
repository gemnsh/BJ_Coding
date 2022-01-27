word=input()
a=[0 for __ in range(26)]
for i in range(26):
    a[i]=word.count(chr(i+65))+word.count(chr(i+97))
max_a=max(a)
alpha=a.index(max(a))
cnt=0
for i in range(26):
    if a[i]==max_a:
        cnt+=1
if cnt>1:
    print('?')
else:
    print(chr(alpha+65))