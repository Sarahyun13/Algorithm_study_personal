import sys
input = sys.stdin.readline

m = int(input())

s = set()

for _ in range(m):
    str = input()
    if(str[1]=='l'):
        s = set([i for i in range(1, 21)])
    elif(str[0]=='e'):
        s.clear()
    else:
        act, numStr = str.split()
        num = int(numStr)

        if act == "add":
            s.add(num)
        elif act == "remove":
            s.discard(num)
        elif act == "check":
            if num in s: print(1)
            else: print(0)
        elif act == "toggle":
            if num in s: s.discard(num)
            else: s.add(num)