import sys
from collections import deque

input = sys.stdin.readline


# 1. BFS
def bfs(num):
    visited = [-1] * (n + 1)
    queue = deque()
    queue.append(num)
    visited[num] = 0

    while queue:
        cur = queue.popleft()

        for next in friends[cur]:
            if visited[next] == -1:
                visited[next] = visited[cur] + 1
                queue.append(next)

    return max(visited)


n = int(input())
friends = [[] for _ in range(n + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    friends[a].append(b)
    friends[b].append(a)

candidate = []
minVal = 51
for i in range(1, n + 1):
    score = bfs(i)
    if score < minVal:
        minVal = score
        candidate = [i]
    elif score == minVal:
        candidate.append(i)

print(minVal, len(candidate))
candidate.sort()
print(*candidate)


# Floyd-Warshall
INF = sys.maxsize
n = int(input())
dp = [[INF] * (n + 1) for _ in range(n + 1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dp[a][b] = 1
    dp[b][a] = 1

for i in range(1, n + 1):
    dp[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j] == 1 or dp[i][j] == 0:
                continue
            elif dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]

result = []
for i in range(1, n + 1):
    result.append(max(a[i][1:]))

minVal = min(result)
print(minVal, result.count(minVal))
for idx, val in enumerate(result):
    if val == minVal:
        print(idx + 1, end=" ")
