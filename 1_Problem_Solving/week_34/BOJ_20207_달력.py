import sys

input = sys.stdin.readline

N = int(input())
calendar = [0] * 366
for _ in range(N):
    S, E = map(int, input().split())
    for i in range(S, E + 1):
        calendar[i] += 1

count, max = 0, 0
result = 0
for idx in range(1, 366):
    if calendar[idx] == 0:
        result += count * max
        max = 0
        count = 0
    else:
        count += 1
        if calendar[idx] > max:
            max = calendar[idx]

result += count * max
print(result)
