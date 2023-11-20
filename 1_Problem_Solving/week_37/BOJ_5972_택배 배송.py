import sys
import heapq

input = sys.stdin.readline


def dijkstra(node):
    queue = []
    heapq.heappush(queue, (0, node))
    distance[node] = 0

    while queue:
        curCow, curNode = heapq.heappop(queue)

        if curCow > distance[curNode]:
            continue

        for nextCow, nextNode in graph[curNode]:
            newCow = curCow + nextCow
            if newCow < distance[nextNode]:
                distance[nextNode] = newCow
                heapq.heappush(queue, (newCow, nextNode))


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, cow = map(int, input().split())
    graph[a].append((cow, b))
    graph[b].append((cow, a))

INF = sys.maxsize
distance = [INF] * (N + 1)
dijkstra(1)

print(distance[N])
