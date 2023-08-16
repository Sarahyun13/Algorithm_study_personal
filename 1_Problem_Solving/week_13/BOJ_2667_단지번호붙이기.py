from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()

    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        curx, cury = queue.popleft()
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1

    return count


countForDfs = 0


def dfs(x, y):
    countForDfs += 1
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            dfs(nx, ny)


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# print()
# print(graph)

# visited = [[False] * N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
town = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            town.append(bfs(i, j))
town.sort()

print(len(town))
for k in town:
    print(k)
