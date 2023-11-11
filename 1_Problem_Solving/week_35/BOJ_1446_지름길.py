import sys
import heapq

input = sys.stdin.readline

N, D = map(int, input().split())

"""
# 1 반복 확인
shortcuts = [list(map(int, input().split())) for _ in range(N)]
distance = [i for i in range(D + 1)]

for i in range(D + 1):
    # 지름길로 간 거리와 고속도로로 간 거리를 비교해서 작은 값 저장
    distance[i] = min(distance[i], distance[i - 1] + 1)

    # 저장된 지름길들을 확인하여 최단 거리 저장
    for start, end, length in shortcuts:
        if i == start and end <= D:
            distance[end] = min(distance[end], distance[i] + length)

print(distance[D])
"""


# 2 heapq 사용 - Dijkstra
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        length, now = heapq.heappop(queue)

        # 이미 입력되어 있는 값이 현재 노드까지의 거리보다 작다면 이미 방문한 노드이므로 넘어감
        if distance[now] < length:
            continue

        # 선택된 현재 노드와 연결된 다른 길 확인
        for i in shortcuts[now]:
            cost = length + i[1]
            # 선택된 길을 거쳐서 이동하는 것이 더 빠른 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


INF = int(1e9)
shortcuts = [[] for _ in range(D + 1)]
distance = [INF] * (D + 1)

# 모든 위치의 거리를 1로 초기화
# 시작 위치 인덱스에 (도착 위치, 길이 1) 저장
for i in range(D):
    shortcuts[i].append((i + 1, 1))

# 지름길이 있는 경우 업데이트
for _ in range(N):
    start, end, length = map(int, input().split())
    if end > D:  # 목적지인 D보다 큰 경우 고려할 필요 없음
        continue
    shortcuts[start].append((end, length))

dijkstra(0)
print(distance[D])
