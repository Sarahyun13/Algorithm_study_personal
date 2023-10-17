import sys
from collections import deque

input = sys.stdin.readline


def findFive(x, y, d):
    queue = deque()
    queue.append((x, y))
    sx, sy = x, y
    count = 1

    while queue:
        x, y = queue.popleft()
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < 19 and 0 <= ny < 19:
            if board[x][y] == board[nx][ny]:
                queue.append((nx, ny))
                count += 1

    if count == 5:
        # print("count = 5")
        nx = sx - dx[d]
        ny = sy - dy[d]
        if 0 <= nx < 19 and 0 <= ny < 19:
            # print(sx, sy, board[sx][sy], end=" ")
            # print(nx, ny, board[nx][ny], end=" ")
            if board[sx][sy] == board[nx][ny]:
                count += 1

    return count


board = [list(map(int, input().split())) for _ in range(19)]
# 가장 왼쪽에 있는 바둑알의 좌표를 출력해야하므로, 마지막 방향은 우상향
dx = [0, 1, 1, -1]
dy = [1, 1, 0, 1]
color, row, col = 0, 0, 0
for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            for d in range(4):
                if findFive(x, y, d) == 5:
                    # print("five!")
                    color = board[x][y]
                    row = x + 1
                    col = y + 1

if not color:
    print(color)
else:
    print(color)
    print(row, col, end=" ")
