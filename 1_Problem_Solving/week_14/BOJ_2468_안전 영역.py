from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y, rain, visit):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1

    while queue:
        curx, cury = queue.popleft()

        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and area[nx][ny] > rain
                and visit[nx][ny] == 0
            ):
                visit[nx][ny] = 1
                queue.append((nx, ny))


N = int(input())
area = []
for _ in range(N):
    area.append(list(map(int, input().split())))

highest = 0
for row in area:
    highest = max(highest, max(row))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0
for rain in range(highest):
    visit = [[0] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if area[i][j] > rain and visit[i][j] == 0:
                bfs(i, j, rain, visit)
                count += 1

    result = max(result, count)

print(result)
