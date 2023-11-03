import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        x = queue.popleft()
        if x == E:
            return visited[E]
        for nx in teleport[x]:
            if visited[nx] > visited[x] + 1:
                queue.append(nx)
                visited[nx] = visited[x] + 1


N, M = map(int, input().split())
S, E = map(int, input().split())
teleport = [[] for _ in range(N + 1)]
teleport[1].append(2)
teleport[N].append(N - 1)
for i in range(2, N):
    teleport[i].append(i - 1)
    teleport[i].append(i + 1)

for _ in range(M):
    x, y = map(int, input().split())
    teleport[x].append(y)
    teleport[y].append(x)

visited = [1e9] * (N + 1)
print(bfs(S))
