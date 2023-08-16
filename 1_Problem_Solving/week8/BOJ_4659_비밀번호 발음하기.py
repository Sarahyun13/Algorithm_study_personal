def findConti(strList):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(strList)-2):
        if strList[i] in vowels and strList[i+1] in vowels and strList[i+2] in vowels:
            return True
        elif strList[i] not in vowels and strList[i+1] not in vowels and strList[i+2] not in vowels:
            return True
        else:
            continue
    
    return False

def findSame(strList):
    for i in range(len(strList)-1):
        if strList[i] == strList[i+1] == 'e' or strList[i] == strList[i+1] == 'o':
            continue
        elif strList[i] == strList[i+1]:
            return True
    
    return False

while(True):
    pw = input()
    if pw == "end": break
    pwList = list(pw)

    if 'a' not in pwList and 'e' not in pwList and 'i' not in pwList and 'o' not in pwList and 'u' not in pwList:
        print("<" + pw + "> is not acceptable.")
    elif findConti(pwList):
        print("<" + pw + "> is not acceptable.")
    elif findSame(pwList):
        print("<" + pw + "> is not acceptable.")
    else:
        print("<" + pw + "> is acceptable.")


