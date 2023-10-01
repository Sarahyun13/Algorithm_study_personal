import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    answer = 0

    while queue:
        x, y = queue.popleft()
        if board[x][y] == "#":
            continue
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == ".":
                # 맨 윗줄로 올라가기만 하면 가장 오른쪽으로 갈 수 있다
                # 1초 뒤에는 욱제와 같은 칸에 있는 벽들이 전부 아래로 내려가고, 욱제는 그 칸에 그대로 있으므로
                if nx == 0:
                    answer = 1
                # 벽이 한 칸 내려오는 것 == 욱제가 한 칸 위로 올라가는 것
                if not visited[nx - 1][ny]:
                    visited[nx - 1][ny] = True
                    queue.append((nx - 1, ny))

    return answer


board = []
for _ in range(8):
    board.append(list(input().rstrip()))

dx = [-1, -1, -1, 0, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, -1, 1, -1, 0, 1, 0]
visited = [[False] * 8 for _ in range(8)]
print(bfs(7, 0))
