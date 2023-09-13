import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True
    count = 0

    while queue:
        y, x = queue.popleft()

        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[y % 2][i]
            if 0 <= ny < H + 2 and 0 <= nx < W + 2:
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                elif graph[ny][nx] == 1:
                    count += 1
    return count


W, H = map(int, input().split())

# 육각형 탐색 문제가 나오면 열과 행에 +2씩 해주어야 한다.
# 밖과 닿는 면을 다 흰색 정육각형으로 둘러준다.
graph = [[0] * (W + 2) for _ in range(H + 2)]
for i in range(1, H + 1):
    graph[i][1 : W + 1] = map(int, input().split())

dy = [0, 1, 1, 0, -1, -1]
# 행 번호가 짝수일 때, 홀수일 때
dx = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]]
visited = [[False] * (W + 2) for _ in range(H + 2)]

print(bfs(0, 0))
