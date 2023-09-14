import sys

input = sys.stdin.readline

N = int(input())
cows = dict()
count = 0
for _ in range(N):
    num, loc = map(int, input().split())
    if num not in cows:
        cows[num] = loc
    else:
        if cows[num] != loc:
            cows[num] = loc
            count += 1

print(count)
