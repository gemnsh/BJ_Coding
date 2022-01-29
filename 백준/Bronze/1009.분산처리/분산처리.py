cnt=int(input())
lst=[[0],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
for _ in range(cnt):
    num=list(map(int,input().split()))
    result =lst[num[0]%10][(num[1]-1)%len(lst[num[0]%10])]
    print(result if result!=0 else 10)