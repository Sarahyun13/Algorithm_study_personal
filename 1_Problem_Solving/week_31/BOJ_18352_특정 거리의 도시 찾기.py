import sys
from collections import deque
import heapq

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

"""
# BFS 풀이
def bfs(start):
    queue = deque([start])
    distance[start] = 0
    answer = []

    while queue:
        cur = queue.popleft()

        for next in graph[cur]:
            if distance[next] == -1:
                distance[next] = distance[cur] + 1
                queue.append(next)
                if distance[next] == K:
                    answer.append(next)

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end="\n")


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
distance = [-1] * (N + 1)
bfs(X)
"""


# Dijkstra 풀이
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, cur = heapq.heappop(queue)

        if distance[cur] < dist:
            continue

        for next in graph[cur]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue, (cost, next[0]))


INF = int(1e9)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
distance = [INF] * (N + 1)
dijkstra(X)
answer = []
for i in range(1, N + 1):
    if distance[i] == K:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i, end="\n")
