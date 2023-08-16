from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        curx, cury = queue.popleft()

        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[curx][cury] == graph[nx][ny]:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

# 적록색약이 아닌 사람
visited = [[False] * (N + 1) for _ in range(N + 1)]
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            bfs(i, j)

print(count, end=" ")

# 적록색약인 사람
for i in range(N):
    for j in range(N):
        if graph[i][j] == "G":
            graph[i][j] = "R"

visited = [[False] * (N + 1) for _ in range(N + 1)]
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            bfs(i, j)

print(count)
