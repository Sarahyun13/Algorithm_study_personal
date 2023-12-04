import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


# 1. Dijkstra 풀이 방법
def dijkstra(node):
    queue = []
    distance = [INF] * (n + 1)
    heapq.heappush(queue, (0, node))
    distance[node] = 0

    while queue:
        curDist, curNode = heapq.heappop(queue)

        if distance[curNode] < curDist:
            continue

        for nextDist, nextNode in graph[curNode]:
            newDist = curDist + nextDist
            if newDist < distance[nextNode]:
                distance[nextNode] = newDist
                heapq.heappush(queue, (newDist, nextNode))

    return distance


n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
    graph[b].append((l, a))

itemMax = 0
for cur in range(1, n + 1):
    itemSum = 0
    distance = dijkstra(cur)

    for next in range(1, n + 1):
        if distance[next] <= m:
            itemSum += items[next]

    itemMax = max(itemMax, itemSum)

print(itemMax)


# 2. Floyd-Warshall 풀이 방법
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

itemMax = 0
for cur in range(1, n + 1):
    itemSum = 0

    for next in range(1, n + 1):
        if graph[cur][next] <= m:
            itemSum += items[next]

    itemMax = max(itemMax, itemSum)

print(itemMax)
