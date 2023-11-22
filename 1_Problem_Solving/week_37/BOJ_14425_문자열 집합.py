import sys

input = sys.stdin.readline

N, M = map(int, input().split())
stringSet = set()
for _ in range(N):
    stringSet.add(input().rstrip())

count = 0
for _ in range(M):
    checkStr = input().rstrip()
    if checkStr in stringSet:
        count += 1

print(count)
