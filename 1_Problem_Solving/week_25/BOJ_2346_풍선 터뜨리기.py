import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
balloon = deque(enumerate(map(int, input().split())))

result = []
while balloon:
    idx, paper = balloon.popleft()
    result.append(idx + 1)

    if paper > 0:
        balloon.rotate(-(paper - 1))
    elif paper < 0:
        balloon.rotate(-paper)

print(*result)
