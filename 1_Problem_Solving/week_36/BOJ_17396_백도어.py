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

# 1e9로 설정하면 너무 작아서 틀림....
# 문제 조건 잘 보기! -> 문제에 t <= 100,000, N <= 100,000 이라 돼있으므로
# 최대 시간으로 모든 분기점을 지날 경우 t*N 값이 나올 수 있다.
# 따라서, 최소 t*N+1 이상으로 잡아야 함.
INF = sys.maxsize
distance = [INF] * (N)
dijkstra(0)
if distance[N - 1] == INF:
    print(-1)
else:
    print(distance[N - 1])
