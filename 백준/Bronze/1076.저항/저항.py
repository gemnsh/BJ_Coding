a=input()
b=input()
c=input()
color_list={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}
print((color_list.get(a)*10+color_list.get(b))*10**color_list.get(c))