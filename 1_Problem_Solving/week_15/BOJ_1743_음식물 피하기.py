import sys

sys.setrecursionlimit(10**7)  # 재귀 깊이 제한 해제
input = sys.stdin.readline


def dfs(x, y):
    global count

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (
            1 <= nx < N + 1
            and 1 <= ny < M + 1
            and aisle[nx][ny] == 1
            and visited[nx][ny] == 0
        ):
            visited[nx][ny] = 1
            count += 1
            dfs(nx, ny)

    return count


N, M, K = map(int, input().split())

aisle = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(K):
    r, c = map(int, input().split())
    aisle[r][c] = 1

visited = [[0] * (M + 1) for _ in range(N + 1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
for x in range(1, N + 1):
    for y in range(1, M + 1):
        if aisle[x][y] == 1 and visited[x][y] == 0:
            visited[x][y] = 1
            count = 1
            result.append(dfs(x, y))

print(max(result))
