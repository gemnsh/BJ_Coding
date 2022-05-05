a=int(input())
b=int(input())
result=0
if a>=b:
    print('Congratulations, you are within the speed limit!')

else:
    if 1<=b-a<=20:
        result=100
    elif 21<=b-a<30:
        result=270
    elif 31<=b-a:
        result=500
    print(f'You are speeding and your fine is ${result}.')