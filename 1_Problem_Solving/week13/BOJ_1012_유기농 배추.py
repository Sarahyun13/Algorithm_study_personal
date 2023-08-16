from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()

    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        curx, cury = queue.popleft()

        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)
