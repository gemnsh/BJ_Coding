n=int(input())
checklist=[]
cmd_name=[]
for _ in range(n):
    cmd_name.append(input())
ex_cmd=list(cmd_name[0])
for j in range(len(cmd_name[0])):
    check=0
    for i in range(n):
        if ex_cmd[j]!=cmd_name[i][j]:
            checklist.append(0)
            check=1
            break
    if check==0:
        checklist.append(1)
for i in range(len(ex_cmd)):
    if checklist[i]==0:
        ex_cmd[i]='?'
print(''.join(ex_cmd))