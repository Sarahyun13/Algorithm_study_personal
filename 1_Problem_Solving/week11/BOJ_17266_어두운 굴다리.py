import sys
import math

input = sys.stdin.readline

N = int(input())
M = int(input())
light = list(map(int, input().split()))

height = max(light[0], N - light[M - 1])

maxGap = 0
for i in range(1, M - 2):
    gap = light[i + 1] - light[i]

    maxGap = max(gap, maxGap)

height = max(math.ceil(maxGap / 2), height)

print(height)
