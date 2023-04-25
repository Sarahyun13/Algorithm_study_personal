# Dijkstra Algorithm (다익스트라 알고리즘)
# 하나의 시작 정점으로부터 모든 다른 정점까지의 <최단 경로>를 찾는 알고리즘
# 음이 아닌 가중 그래프에서의 단일 쌍, 단일 출발, 단일 도착 최단 경로 문제
# 1. dist 배열 INF로 초기화
# 2. 시작점 입력 받고, dist[시작점]=0, visit[시작점]=true 로 설정 (탐색 방법)
#		시작점 입력 받고, dist[시작점]=0, pq에 {0, 시작점} 삽입 (우선순위 큐 방법)
# 3. dist 배열에서 최소 비용 정점을 찾고 visit 처리, 이미 방문한 노드는 제외. (탐색 방법)
#		pq.empty() 될 때까지 (우선순위 큐 방법)
#		-> pq.front() = {거리 비용, 노드 인덱스}
#		-> dist[노드 인덱스] < 거리 비용 이면 이미 체크한 경우이므로 패스
# 4. 새로운 정점을 거쳐 갈 수 있는 거리가 기존 거리보다 작다면 거리값 갱신

INF = int(1e9)

n, m = map(int, input().split()) # 노드 개수, 간선 개수
start = int(input()) # 시작 노드
visited = [False] * (n+1) # 방문 체크
distance = [INF] * (n+1) # 최단거리 테이블

graph = [[] for _ in range(n+1)] # 노드 연결 정보 리스트
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a노드에서 b 노드로 가는 비용이 c

# 1. 우선순위 큐 사용하지 않고 직접 탐색하는 방법 (시간복잡도는 O(V^2))
# 방문하지 않은 노드이면서 시작노드와 최단 거리인 노드 반환
def smallestNode():
    minVal = INF
    index = 0 # 최단 거리인 노드 인덱스
    for i in range(1, n+1):
        if distance[i] < minVal and not visited[i]:
            minVale = distance[i]
            index = i

    return index

def dijkstra1(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1] # 시작 노드와 연결된 노드들의 거리 입력

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리인 노드를 꺼내서 방문 처리
        now = smallestNode()
        visited[now] = True

        # 선택된 현재 노드와 연결된 다른 노드를 확인
        for j in range[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 2. 우선순위 큐(최소 힙)를 사용하는 방법 (시간복잡도는 O(ElogE)) -> 더 빠름
import heapq

def dijkstra2(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # q가 빌 때까지
    while q:
        # 최단 거리인 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 별도의 visited 테이블이 필요 없이, 최단 거리 테이블을 이용해 방문 여부 확인
        # 이미 입력되어 있는 값이 현재 노드까지의 거리보다 작다면 이미 방문한 노드이므로 넘어감
        if distance[now] < dist:
            continue

        # 선택된 현재 노드와 연결된 다른 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 선택된 현재 노드를 거쳐서 이동하는 것이 더 빠른 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


