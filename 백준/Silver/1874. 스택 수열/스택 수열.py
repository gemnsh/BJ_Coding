N=int(input())
result=[int(input())for _ in range(N)]
start=list(range(N,0,-1))
stack=[]
index=0
output_result=[]
chck=True
while 1:
    if stack:
        if stack[-1]==result[index]:
            tmp=stack.pop()
            result.append(tmp)
            index+=1
            output_result.append('-')
        else:
            if start:
                tmp=start.pop()
                stack.append(tmp)
                output_result.append('+')
            else:
                chck=False
                break
    else:
        if start:
            tmp=start.pop()
            stack.append(tmp)
            output_result.append('+')
        else:
            chck=False
            break
    if index==N:
        break
if chck:
    print(*output_result,sep='\n')
else:
    print('NO')
