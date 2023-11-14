import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tech = list(map(int, input().split()))
cards = deque()
for i in range(len(tech) - 1, -1, -1):
    if tech[i] == 1:
        cards.appendleft(N - i)
    elif tech[i] == 2:
        cards.insert(1, N - i)
    elif tech[i] == 3:
        cards.append(N - i)

print(*cards)
