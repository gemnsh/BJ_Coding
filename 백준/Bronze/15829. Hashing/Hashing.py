L=int(input())
string_input=input()
result=0
for i in range(L):
    tmp=ord(string_input[i])-96
    result+=(tmp*(31**i))
print(result%1234567891)