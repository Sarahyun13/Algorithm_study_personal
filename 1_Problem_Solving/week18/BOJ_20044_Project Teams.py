import sys

input = sys.stdin.readline

n = int(input())
ability = list(map(int, input().split()))

ability.sort()

minVal = 1e9
for i in range(n):
    sum = ability[i] + ability[2 * n - 1 - i]
    minVal = min(minVal, sum)

print(minVal)
