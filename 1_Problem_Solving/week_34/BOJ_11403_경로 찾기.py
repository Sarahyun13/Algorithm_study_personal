import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for row in graph:
    print(*row)


# BFS
# def bfs(x):
#     queue = deque()
#     queue.append(x)
#     check = [0 for _ in range(N)]

#     while queue:
#         nx = queue.popleft()

#         for i in range(N):
#             if check[i] == 0 and graph[nx][i] == 1:
#                 queue.append(i)
#                 check[i] = 1
#                 visited[x][i] = 1


# visited = [[0] * N for _ in range(N)]
# for i in range(0, N):
#     bfs(i)

# for row in visited:
#     print(*row)
