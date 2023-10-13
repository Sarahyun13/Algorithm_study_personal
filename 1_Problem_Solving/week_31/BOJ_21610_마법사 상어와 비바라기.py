import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
buckets = [list(map(int, input().split())) for _ in range(N)]
cloudList = deque([(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)])
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(M):
    d, s = map(int, input().split())

    # 구름이 이동하고 비가 내린다
    rainList = deque()
    for _ in range(len(cloudList)):
        x, y = cloudList.popleft()  # 이동시키면서 구름리스트에서 구름은 사라진다
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        # print(nx, ny)
        rainList.append((nx, ny))  # 모든 구름이 d 방향으로 s칸 이동하고, 비리스트에 저장한다.
        buckets[nx][ny] += 1  # 구름에서 비가 내려 구름이 있는 칸의 바구니에 물이 1 증가한다.

    # 물이 증가한 칸들(r, c)에 물복사버그 마법을 시전한다.
    verx = [-1, -1, 1, 1]
    very = [-1, 1, 1, -1]
    for i in range(len(rainList)):
        x, y = rainList[i]
        for v in range(4):
            nx = x + verx[v]
            ny = y + very[v]

            # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)칸 바구니의 물이 증가한다.
            if 0 <= nx < N and 0 <= ny < N and buckets[nx][ny] > 0:
                buckets[x][y] += 1

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    # 방금 전 구름이 사라진 칸들은 제외하고 구름이 생겨야 한다.
    for x in range(N):
        for y in range(N):
            if buckets[x][y] >= 2 and (x, y) not in rainList:
                buckets[x][y] -= 2
                cloudList.append((x, y))

total = 0
for row in buckets:
    total += sum(row)

print(total)
