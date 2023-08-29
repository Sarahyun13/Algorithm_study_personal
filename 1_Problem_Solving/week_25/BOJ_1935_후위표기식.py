import sys

input = sys.stdin.readline

N = int(input())
string = input().rstrip()

alph = {}
for i in range(N):
    a = chr(ord("A") + i)
    alph[a] = int(input())

# print(alph)
stack = []
for s in string:
    if "A" <= s <= "Z":
        stack.append(alph[s])
    else:
        y = stack.pop()
        x = stack.pop()

        if s == "+":
            stack.append(x + y)
        elif s == "-":
            stack.append(x - y)
        elif s == "*":
            stack.append(x * y)
        elif s == "/":
            stack.append(x / y)

# print("%.2f" % stack[0])
print("{:.2f}".format(stack[0]))
