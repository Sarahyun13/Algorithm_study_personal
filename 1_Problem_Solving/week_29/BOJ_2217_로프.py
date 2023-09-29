import sys

input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort()
maxWeight = 0
for i in range(N):
    if ropes[i] * (N - i) > maxWeight:
        maxWeight = ropes[i] * (N - i)

print(maxWeight)
