d,h,w=map(int,input().split())
real_h=(((d**2)/(h**2+w**2))**0.5)*h
real_w=(((d**2)/(h**2+w**2))**0.5)*w
print(f'{int(real_h)} {int(real_w)}')