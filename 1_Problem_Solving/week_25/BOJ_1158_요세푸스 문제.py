import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque()
result = []

for i in range(1, N + 1):
    queue.append(i)

# print(queue)

while queue:
    for k in range(K):
        if k == K - 1:
            result.append(queue.popleft())
        else:
            queue.append(queue.popleft())

print(str(result).replace("[", "<").replace("]", ">"))
