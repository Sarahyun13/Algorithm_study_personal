from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    paper[x][y] = 1
    area = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and paper[nx][ny] == 0:
                paper[nx][ny] = 1
                area += 1
                queue.append((nx, ny))

    return area


M, N, K = map(int, input().split())
paper = [[0] * N for _ in range(M)]
for _ in range(K):
    sy, sx, ey, ex = map(int, input().split())

    for x in range(sx, ex):
        for y in range(sy, ey):
            paper[x][y] = -1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 0
result = []
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            count += 1
            result.append(bfs(i, j))

result.sort()
print(count)
for val in result:
    print(val, end=" ")
