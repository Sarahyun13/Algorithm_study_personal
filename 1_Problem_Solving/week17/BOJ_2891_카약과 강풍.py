import sys

input = sys.stdin.readline

N, S, R = map(int, input().split())
lost = list(map(int, input().split()))
spare = list(map(int, input().split()))

kayak = [1] * (N + 1)
for i in range(1, N + 1):
    if i in lost:
        kayak[i] -= 1
    if i in spare:
        kayak[i] += 1

for i in range(1, N + 1):
    if i == 1:
        if kayak[i] == 0 and kayak[i + 1] == 2:
            kayak[i] = 1
            kayak[i + 1] = 1
    elif i == N:
        if kayak[i] == 0 and kayak[i - 1] == 2:
            kayak[i] = 1
            kayak[i - 1] = 1
    else:
        if kayak[i] == 0:
            if kayak[i - 1] == 2:
                kayak[i] = 1
                kayak[i - 1] = 1
            elif kayak[i + 1] == 2:
                kayak[i] = 1
                kayak[i + 1] = 1

print(kayak.count(0))
