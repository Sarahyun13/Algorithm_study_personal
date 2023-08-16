import sys

input = sys.stdin.readline


def dfs(x, y, r, pre):
    if x == N - 1:
        global result
        result = min(result, r)
        return

    d = [-1, 0, 1]
    for k in range(3):
        if 0 <= y + d[k] < M and k != pre:
            dfs(x + 1, y + d[k], r + matrix[x + 1][y + d[k]], k)


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = 1e9

for i in range(M):
    dfs(0, i, matrix[0][i], -1)

print(result)
