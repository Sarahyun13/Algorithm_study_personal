from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                queue.append((nz, nx, ny))


M, N, H = map(int, input().split())

box = []
for _ in range(H):
    tomato = []
    for _ in range(N):
        tomato.append(list(map(int, input().split())))

    box.append(tomato)

queue = deque()
for z in range(H):  # 높이
    for x in range(N):  # 행
        for y in range(M):  # 열
            if box[z][x][y] == 1:
                queue.append((z, x, y))

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

bfs()

result = 0
for a in box:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        result = max(result, max(b))

print(result - 1)
