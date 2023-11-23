import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(s):
    queue = []
    heapq.heappush(queue, (0, s))
    distance[s] = 0

    while queue:
        curDist, curNode = heapq.heappop(queue)
        if curDist > distance[curNode]:
            continue

        for nextDist, nextNode in edges[curNode]:
            newDist = curDist + nextDist
            if newDist < distance[nextNode]:
                distance[nextNode] = newDist
                heapq.heappush(queue, (newDist, nextNode))


n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

s, t = map(int, input().split())
distance = [INF] * (n + 1)
dijkstra(s)
print(distance[t])
