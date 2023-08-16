from collections import deque
import sys

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

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if iceberg[nx][ny] != 0:  # 빙산이라면
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif iceberg[nx][ny] == 0:  # 바닷물이라면
                    ocean[x][y] += 1  # 접해 있는 바닷물 개수 증가


N, M = map(int, input().split())
iceberg = []
for _ in range(N):
    iceberg.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while True:
    count = 0  # 빙산 개수
    ocean = [[0] * M for _ in range(N)]  # 접해 있는 바닷물 개수
    visited = [[False] * M for _ in range(N)]

    for x in range(N):
        for y in range(M):
            if iceberg[x][y] != 0 and not visited[x][y]:
                bfs(x, y)
                count += 1  # 빙산 개수

    if count >= 2:  # 빙산이 2개 이상으로 분리됐다면
        print(time)  # 최초로 분리된 시간(년) 출력
        break
    elif count == 0:  # 빙산이 다 녹을 때까지 분리되지 않았다면
        print(0)  # 0 출력
        break

    time += 1  # 시간(년) 증가

    # 빙산 녹이기
    for x in range(N):
        for y in range(M):
            iceberg[x][y] -= ocean[x][y]
            if iceberg[x][y] < 0:  # 0보다 작아진다면
                iceberg[x][y] = 0  # 0으로 만들어 줌
