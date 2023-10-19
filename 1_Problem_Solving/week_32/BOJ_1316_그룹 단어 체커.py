import sys

input = sys.stdin.readline

N = int(input())
count = 0
for _ in range(N):
    word = input().rstrip()
    alpha = []
    group = True
    for i in range(len(word)):
        if word[i] not in alpha:
            alpha.append(word[i])
        elif word[i] in alpha and word[i] != word[i - 1]:
            group = False

    if group:
        count += 1

print(count)
