# Prim Algorithm (프림 알고리즘)
# 대표적인 Minimum Spanning Tree(MST 최소 신장 트리) 알고리즘
# Spanning tree(신장 트리)란 하나의 무방향 가중치 그래프가 있을 때 그래프 내의 모든 정점을 포함하면서 사이클이 존재하지 않는 부분 그래프이자 트리이다.
# 하나의 그래프에는 많은 신장 트리가 존재 가능한데,
# 그 중에서도 간선들의 가중치 합이 최소인 신장 트리를 최소 신장 트리(Minimum Spanning Tree - MST)라 한다.
# 신장 트리는 그래프에 있는 n개의 정점을 정확히 (n-1)개의 간선으로 연결하게 된다.
# 프림 알고리즘의 시간복잡도는 최소 힙구조를 사용하는 경우 O(ElogV)이고, 사용하지 않는 경우 O(V^2)이다.

# Kruskal 알고리즘과이 차이
# -> Kruskal 알고리즘은 간선을 기반으로 하는 알고리즘인 반면 Prim 알고리즘은 정점을 기반으로 하는 알고리즘
# -> Kruskal 알고리즘은 이전 단계에서 만들어진 신장 트리와는 상관없이 무조건 최저 간선만을 선택하는 방법이었지만
#    Prim 알고리즘은 이전 단계에서 만들어진 신장 트리를 확장하는 방식
# 그래프 내의 간선이 적은 경우는 Kruskal 알고리즘, 간선이 많은 경우는 Prim 알고리즘이 유리하다.

# 1. 임의의 정점을 시작점으로 선택하고, 트리 집합에 넣는다.
# 2. 트리 집합에 속한 정점들과 인접한 정점들 중 가장 가중치가 작은 정점과 간선을 트리 집합에 넣는다.
# 3. 사이클 발생을 막기 위해 연결된 정점이 이미 트리 집합에 속한다면 그 다음 가중치가 작은 정점과 간선을 트리 집합에 넣는다.
# 4. -> 반복한다.

import heapq
import collections

def prim(edges, start):
    connected = set(start) # 처음 선택한 노드를 트리 집합에 삽입
    candidate = edges[start] # 인접 간선들을 후보 간선에 삽입
    heapq.heapify(candidate) # 우선순위 큐 생성

    mst = []
    while candidate:
        weight, u, v = heapq.heappop(candidate) # 가중치가 가장 작은 간선 선택
        
        if v not in connected: # 트리 집합에 없는 노드라면
            connected.add(v) # 트리 집합에 삽입
            mst.append((weight, u, v)) # mst에 삽입

            for edge in edges[v]: # 다음 인접 간선 탐색
                if edge[2] not in connected: # 트리 집합에 없는 노드라면 (사이클 방지)
                    heapq.heappush(candidate, edge) # 우선순위 큐에 삽입

    return mst

# 노드, 간선 개수 입력 받기
v, e = map(int, input().split())

# 간선에 대한 정보를 담는 리스트
edges = collections.defaultdict(list)
# 무방향 그래프 생성
for i in range(e): # 간선 정보 입력 받기
    u, v, weight = map(int, input().split()) # 정점1, 정점2, 가중치
    edges[u].append([weight, u, v])
    edges[v].append([weight, v, u])

print(prim(edges, 1))