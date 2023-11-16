import sys

input = sys.stdin.readline

# a*(b+c) = a*b + a*c 원리 이용
string = input().rstrip()
stack = []
result = 0
partial = 1
for i in range(len(string)):
    if string[i] == "(":
        stack.append(string[i])
        partial *= 2
    elif string[i] == "[":
        stack.append(string[i])
        partial *= 3
    elif string[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if string[i - 1] == "(":
            result += partial
        stack.pop()
        partial //= 2
    elif string[i] == "]":
        if not stack or stack[-1] == "(":
            result = 0
            break
        if string[i - 1] == "[":
            result += partial
        stack.pop()
        partial //= 3

if stack:
    print(0)
else:
    print(result)
