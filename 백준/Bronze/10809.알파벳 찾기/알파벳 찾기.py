S=input()
string_save=[]
for i in range(97,123):
    string_save.append(S.find(chr(i)))
for i in string_save:
    print(i,end=' ')