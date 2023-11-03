import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == M - 1:
                return True

            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                if fiber[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

    return False


M, N = map(int, input().split())
fiber = []
for _ in range(M):
    fiber.append(list(map(int, input().rstrip())))

# print(fiber)

visited = [[False] * N for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for y in range(N):
    if fiber[0][y] == 0:
        if bfs(0, y):
            print("YES")
            exit()
print("NO")
