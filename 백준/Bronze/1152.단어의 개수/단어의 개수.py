word=input()
word=word.strip()
if word=='':
    print(0)
else:
    print(word.count(' ')+1) 