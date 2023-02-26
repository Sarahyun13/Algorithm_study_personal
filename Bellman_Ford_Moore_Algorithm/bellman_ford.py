# Bellman Ford Moore Algorithm (벨만-포드 알고리즘)
# 하나의 시작 정점으로부터 모든 다른 정점까지의 <최단 경로>를 찾는 알고리즘
# 음의 가중치를 가지는 간선도 가능
# 음의 사이클의 존재 여부를 확인할 수 있다
# 최단거리를 구하기 위해 V-1번 E개의 모든 간선을 확인한다.
# 음의 사이클 존재 여부를 확인하기 위해 한 번 더 E개의 간선을 확인한다.
# V개의 정점과 E개의 간선을 가진 가중 그래프에서 시작 정점에서 특정 정점까지의 최단 거리는 최대 V-1개의 간선을 사용한다.
# 그러므로 V번째 간선이 추가되어 거리배열이 갱신되는 순간 사이클이라고 판단할 수 있다.
# 총 연산 횟수는 VE이므로 시간 복잡도는 O(VE)이다.

# 1. 최단 거리 배열 dist를 INF로 초기화, 시작 정점은 0으로 초기화
# 2. 전체 간선 E개를 하나씩 확인하고,
#    각 간선을 거쳐 다른 노드로 가는 거리가 더 짧은 경우, 최단 거리 배열 갱신
# => 2번 과정을 V-1번 반복
# 3. V-1번 반복 이후, V번째 반복에서도 최단 거리 배열이 갱신된다면 음수 순환이 존재하는 것

INF = int(1e9) # 무한대 값

def bellmanFord(start):
    dist[start] = 0 # 시작 정점은 0으로 초기화

    # V-1번 탐색하고 마지막 한 번은 음의 사이클 존재 확인 -> 총 V번
    for i in range(v):
        # 매 반복마다 전체 간선 E개를 확인
        for j in range(e):
            curNode, nextNode, edgeCost = edges[j]

            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[curNode] != INF and dist[curNode] + edgeCost < dist[nextNode]:
                dist[nextNode] = dist[curNode] + edgeCost # 최단 거리 배열 갱신
                
                # V번째 반복에서 갱신되는 값이 있으면 음수 순환이 존재
                if i == v-1:
                    return False

    return True


# 노드, 간선 개수 입력 받기
v, e = map(int, input().split())

# 간선에 대한 정보를 담는 리스트
edges = []
for _ in range(e):
    v1, v2, cost = map(int, input().split()) # 정점1, 정점2, 가중치
    edges.append((v1, v2, cost))

# 최단 거리 테이블을 무한대로 초기화
dist = [INF] * (v+1)

# 1번 정점을 시작노드로 하고 벨만 포드 알고리즘 수행
if bellmanFord(1): # true라면 정상 종료된 것
    # 1번 정점을 제외한 다른 모든 정점으로 가기 위한 최단 거리 출력
    for i in range(2, v+1):
        if dist[i] == INF: # 도달할 수 없는 경우
            print("There's no way to go") # 갈 수 없음을 출력
        else: # 도달할 수 있는 경우
            print(dist[i]) # 거리 출력
else: # false라면 음의 사이클 존재
    print("Negative Cycle exist")