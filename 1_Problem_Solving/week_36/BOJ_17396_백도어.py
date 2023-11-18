import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        curTime, curNode = heapq.heappop(queue)

        if curTime > distance[curNode]:
            continue

        for nextTime, nextNode in graph[curNode]:
            newTime = curTime + nextTime
            if newTime < distance[nextNode] and not sight[nextNode]:
                distance[nextNode] = newTime
                heapq.heappush(queue, (newTime, nextNode))


N, M = map(int, input().split())
sight = list(map(int, input().split()))
sight[-1] = 0
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))
    graph[b].append((t, a))

INF = sys.maxsize
distance = [INF] * (N)
dijkstra(0)
if distance[N - 1] == INF:
    print(-1)
else:
    print(distance[N - 1])
