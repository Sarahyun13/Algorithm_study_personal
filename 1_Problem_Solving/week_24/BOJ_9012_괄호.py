import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    stack = []
    string = input().rstrip()

    if string[0] == ")":
        print("NO")
        continue

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(string[i])
        elif stack and string[i] == ")":
            stack.pop()
        else:
            stack.append(string[i])
            break

    # print(stack)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
