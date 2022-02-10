while 1:
    string_new=input()
    if string_new=='.':
        break
    else:
        check=[]
        dsc=[] # True 면 (
        result=True
        for i in range(len(string_new)):
            if string_new[i]=='[' :
                check.append(string_new[i])
                dsc.append(False)
            elif string_new[i]=='(' :
                check.append(string_new[i])
                dsc.append(True)
            elif string_new[i]==')' :
                if dsc:
                    if dsc.pop()==True:
                        check.pop()
                    else:
                        result=False
                        break
                else:
                    result=False
                    break
            elif string_new[i]==']':
                if dsc:
                    if dsc.pop()==False:
                        check.pop()
                    else:
                        result=False
                        break
                else:
                    result=False
                    break
        if dsc==[] and check==[] and result==True:
            result=True
        else:
            result=False
        print("yes"if result else "no")
