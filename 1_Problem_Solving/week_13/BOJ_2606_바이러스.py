from collections import deque
import sys

input = sys.stdin.readline


def bfs(v):
    global count
    queue = deque()

    queue.append(v)
    visited[v] = True

    while queue:
        cur = queue.popleft()

        for next in graph[cur]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                count += 1


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n + 1)
count = 0

bfs(1)
print(count)
