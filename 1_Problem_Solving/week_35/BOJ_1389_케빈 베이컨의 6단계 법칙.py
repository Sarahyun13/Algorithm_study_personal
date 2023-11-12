import sys
from collections import deque

input = sys.stdin.readline

# Floyd-Warshall
N, M = map(int, input().split())
relationship = [[N] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    relationship[a][b] = 1
    relationship[b][a] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a == b:  # 자기 자신
                relationship[a][b] = 0
            else:
                relationship[a][b] = min(
                    relationship[a][b], relationship[a][k] + relationship[k][b]
                )

answer = []
for row in relationship:
    answer.append(sum(row))
print(answer.index(min(answer)))


# BFS
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start] = 1

#     while queue:
#         a = queue.popleft()

#         for b in friends[a]:
#             if not visited[b]:
#                 visited[b] = visited[a] + 1
#                 queue.append(b)


# N, M = map(int, input().split())
# friends = [[] for _ in range(N + 1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     friends[a].append(b)
#     friends[b].append(a)

# answer = []
# for i in range(1, N + 1):
#     visited = [0] * (N + 1)
#     bfs(i)
#     answer.append(sum(visited))

# print(answer.index(min(answer)) + 1)
