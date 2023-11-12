import sys

input = sys.stdin.readline

N = int(input())
count = 0
for _ in range(N):
    stack = []
    word = input().rstrip()
    for i in range(len(word)):
        if stack and stack[-1] == word[i]:
            stack.pop()
        else:
            stack.append(word[i])

    if not stack:
        count += 1

print(count)
