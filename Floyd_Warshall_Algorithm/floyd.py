# Floyd Warshall Algorithm (플로이드-워셜 알고리즘)
# 그래프에 존재하는 모든 정점 사이의 <최단 경로>를 찾는 알고리즘
# 어떤 두 정점 A, B 사이의 최단 경로는 어떤 경유 정점 K를 거치거나 거치지 않는 경로 중 하나이다.
# 즉, 정점 A와 정점 B 사이의 최단 경로는 A->B 이거나 A->K->B 이다.
# 만약, 경유 정점 K를 거친다면 최단 경로를 이루는 부분 경로 역시 최단 경로이다.
# 다시 말해, 만약 A->B의 최단 경로가 A->K->B 라면 A->K와 K->B도 각각 최단 경로이다.
# 최단 거리를 갱신할 때 점화식을 사용하므로 Dynamic Programming(동적 계획법)이 적용된다.
# 다른 최단경로 알고리즘(다익스트라, 벨만포드)들과는 다르게 모든 정점에서 모든 정점으로 가는 최단 경로를 구하므로 2차원 리스트를 사용한다.
# 모든 정점에서 모든 정점으로 가는 최단 경로를 구하므로 시간 복잡도는 O(V^3)이다.

# 1. 최단 거리 테이블 dist 내 특정 정점에서 자기 자신으로 가는 비용은 항상 0이므로 대각 행렬의 값은 모두 0으로 초기화
# 2. 특정 정점에서 다른 정점으로 가는 비용에 따라 최단 거리 테이블을 갱신
# 3. 두 정점 사이에 간선이 없다면 INF로 초기화
# 4. 1번 정점부터 차례대로 해당 노드를 중간에 거쳐서 가는 모든 노드 간의 최단 경로를 계산하고 최단 거리 테이블 갱신

INF = int(1e9) # 무한대 값

# floyd 알고리즘
def floyd():
    for k in range(1, v+1):
        for a in range(1, v+1):
            for b in range(1, v+1):
                # a->b 와 a->k->b 중 더 짧은 경로 값 저장
                dist[a][b] = min(dist[a][b], dist[a][k]+dist[k][b])


# 노드, 간선 개수 입력 받기
v, e = map(int, input().split())

# INF로 초기화한 최단 거리 배열
dist = [[INF]*(v+1) for _ in range(v+1)]

# 자기 자신으로 가는 거리 비용은 항상 0이므로 대각 행렬의 값 0으로 초기화
for i in range(1, v+1):
    for j in range(1, v+1):
        if i == j:
            dist[i][j] = 0

# 간선에 대한 정보를 입력 받아 dist 갱신
for _ in range(e):
    v1, v2, cost = map(int, input().split()) # 정점1, 정점2, 가중치
    dist[v1][v2] = cost

# floyd 알고리즘 수행
floyd()
# 최단 거리 테이블 출력
for i in range(1, v+1):
    for j in range(1, v+1):
        if dist[i][j] == INF: # 경로가 없다면
            print("INF") # 무한대 출력
        else: # 최단 경로가 존재한다면
            print(dist[i][j], end=' ') # 최단 거리 출력
    print() # 줄 바꿈