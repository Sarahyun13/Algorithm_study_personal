import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[0] * M for _ in range(N)]
    sword = 1e9

    while queue:
        x, y = queue.popleft()

        # 공주가 있는 곳에 도착했을 경우,
        # 칼이 없을 때와 있을 때 중 최소 거리 리턴
        if x == N - 1 and y == M - 1:
            return min(visited[x][y], sword)

        # 칼이 있는 곳에 도착했을 경우,
        # 그 이후로는 공주한테까지 아무 제약 없이 갈 수 있고,
        # 도착만 하면 되므로
        # 칼이 있는 곳까지 걸린 시간 + 칼에서 공주까지 남아있는 칸 수만큼 더해줌
        if castle[x][y] == 2:
            sword = visited[x][y] + N - 1 - x + M - 1 - y

        # 칼이 없을 때를 고려해 계속해서 bfs 수행
        # 칼이 있을 때는 최단거리가 정해져 있으므로 할 필요 없음
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < M
                and castle[nx][ny] != 1
                and visited[nx][ny] == 0
            ):
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    # 공주한테까지 못갔을 경우
    return sword


N, M, T = map(int, input().split())
castle = []
for _ in range(N):
    castle.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = bfs(0, 0)
if result <= T:
    print(result)
else:
    print("Fail")
