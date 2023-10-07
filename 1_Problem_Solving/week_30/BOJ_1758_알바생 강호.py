import sys

input = sys.stdin.readline

N = int(input())
tips = []
for _ in range(N):
    tips.append(int(input()))
tips.sort(reverse=True)

# print(tips)
for i in range(len(tips)):
    tips[i] -= i
    if tips[i] < 0:
        tips[i] = 0

# print(tips)
print(sum(tips))
