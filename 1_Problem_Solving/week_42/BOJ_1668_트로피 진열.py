import sys

input = sys.stdin.readline

N = int(input())
trophies = list(int(input()) for _ in range(N))

# left
high = trophies[0]
count = 1
for i in range(1, N):
    if trophies[i] > high:
        count += 1
        high = trophies[i]

print(count)

# right
high = trophies[N - 1]
count = 1
for i in range(N - 2, -1, -1):
    if trophies[i] > high:
        count += 1
        high = trophies[i]

print(count)
