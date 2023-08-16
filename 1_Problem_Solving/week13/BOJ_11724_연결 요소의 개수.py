from collections import deque
import sys

input = sys.stdin.readline


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        x = queue.popleft()

        for nx in graph[x]:
            if not visited[nx]:
                queue.append(nx)
                visited[nx] = True


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)

count = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)
