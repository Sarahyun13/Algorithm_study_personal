import sys
import heapq

input = sys.stdin.readline


def dijkstra(bus, start):
    distance[start] = 0  # 자기 자신은 0
    queue = []
    heapq.heappush(queue, [0, start])  # 시작 노드부터 탐색

    while queue:
        curCost, curNode = heapq.heappop(queue)  # 탐색할 노드와 거리
        if distance[curNode] < curCost:  # 기존 최단 거리보다 크다면
            continue  # 무시

        for nextNode, nextCost in bus[curNode]:
            newCost = curCost + nextCost
            if distance[nextNode] > newCost:
                distance[nextNode] = newCost
                heapq.heappush(queue, [newCost, nextNode])


N = int(input())
M = int(input())
bus = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    bus[start].append((end, cost))
start, end = map(int, input().split())

distance = [1e9] * (N + 1)
dijkstra(bus, start)
print(distance[end])
