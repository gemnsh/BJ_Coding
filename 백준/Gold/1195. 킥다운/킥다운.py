A=input()
B=input()
if len(B)>len(A):
    A,B=B,A
A=A.replace('1','0')
A=A.replace('2','1')
B=B.replace('1','0')
B=B.replace('2','1')
answer=len(A)+len(B)
for i in range(1,len(A)+len(B)):
    tmp,tmp_a=0,0
    if i<=len(B):
        tmp='0b'+B[len(B)-i:len(B)]
        tmp_a='0b'+A[0:i]
    elif len(B)<i<len(A):
        tmp='0b'+B
        tmp_a='0b'+A[i-len(B):i]
    else:
        tmp='0b'+B[0:len(A)+len(B)-i]
        tmp_a='0b'+A[-1*(len(tmp)-2):]
    result=bin(int(tmp,2) & int(tmp_a,2))
    if int(result,2)==0:
        tmp_result=len(A)+len(B)
        if i<=len(B):
            tmp_result=len(A)+len(B)-i
        elif i<=len(A):
            tmp_result=len(A)
        else:
            tmp_result=len(A)+len(B)-len(tmp)+2
        if tmp_result<answer:
            answer=tmp_result
print(answer)