a,b=input().split()
a=list(a)
b=list(b)
a.reverse()
b.reverse()
new_a=int(''.join(a))
new_b=int(''.join(b))
if new_a>new_b:
    print(new_a)
elif new_b>new_a:
    print(new_b)