import sys

input = sys.stdin.readline

N, M = map(int, input().split())
bulbs = list(map(int, input().split()))
for _ in range(M):
    a, b, c = map(int, input().split())

    if a == 1:
        bulbs[b - 1] = c
    elif a == 2:
        for i in range(b - 1, c):
            bulbs[i] = (bulbs[i] + 1) % 2
    elif a == 3:
        bulbs[b - 1 : c] = [0] * (c - b + 1)
    elif a == 4:
        bulbs[b - 1 : c] = [1] * (c - b + 1)

print(*bulbs)
