num=int(input())
cup=1
for _ in range(num):
    exchange=list(map(int, input().split()))
    if cup in exchange:
        if cup==exchange[0]:
            cup=exchange[1]
        else:
            cup=exchange[0]
print(cup)