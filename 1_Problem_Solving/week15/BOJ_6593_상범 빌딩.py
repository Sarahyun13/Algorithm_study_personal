from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]


def bfs(z, x, y):
    queue = deque()
    queue.append((z, x, y))
    visited[z][x][y] = 1

    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if building[nz][nx][ny] == "E":
                    print("Escaped in {} minute(s).".format(visited[z][x][y]))
                    return
                if building[nz][nx][ny] == "." and visited[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    queue.append((nz, nx, ny))

    print("Trapped!")


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = [[] * R for _ in range(L)]
    for z in range(L):
        for x in range(R):
            building[z].append(list(input().rstrip()))
        input()

    visited = [[[0] * C for _ in range(R)] for _ in range(L)]

    for z in range(L):
        for x in range(R):
            for y in range(C):
                if building[z][x][y] == "S":
                    bfs(z, x, y)
