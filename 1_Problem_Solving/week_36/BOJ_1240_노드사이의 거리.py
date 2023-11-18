import sys
from collections import deque

input = sys.stdin.readline


def bfs(a, b):
    queue = deque()
    distance = [-1] * (N + 1)
    queue.append(a)
    distance[a] = 0

    while queue:
        now = queue.popleft()
        if now == b:
            return distance[b]

        for next, dist in tree[now]:
            if distance[next] == -1:
                distance[next] = distance[now] + dist
                queue.append(next)


N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, dist = map(int, input().split())
    tree[a].append((b, dist))
    tree[b].append((a, dist))

for _ in range(M):
    a, b = map(int, input().split())
    print(bfs(a, b))
