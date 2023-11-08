import sys

input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == ".":
        break

    stack = []
    balance = True
    for c in string:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                balance = False
        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                balance = False

    if stack or not balance:
        print("no")
    else:
        print("yes")
