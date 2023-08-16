from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))


testCase = int(input())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(testCase):
    l = int(input())
    board = [[0] * l for _ in range(l)]

    x, y = map(int, input().split())
    board[x][y] = 1
    ex, ey = map(int, input().split())

    bfs(x, y)
    print(board[ex][ey] - 1)
