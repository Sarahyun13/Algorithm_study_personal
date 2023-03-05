# Kruskal Algorithm (크루스칼 알고리즘)
# 대표적인 Minimum Spanning Tree(MST 최소 신장 트리) 알고리즘
# Spanning tree(신장 트리)란 하나의 무방향 가중치 그래프가 있을 때 그래프 내의 모든 정점을 포함하면서 사이클이 존재하지 않는 부분 그래프이자 트리이다.
# 하나의 그래프에는 많은 신장 트리가 존재 가능한데,
# 그 중에서도 간선들의 가중치 합이 최소인 신장 트리를 최소 신장 트리(Minimum Spanning Tree - MST)라 한다.
# 신장 트리는 그래프에 있는 n개의 정점을 정확히 (n-1)개의 간선으로 연결하게 된다.
# 크루스칼 알고리즘은 Greedy Algorithm과 Union-Find 알고리즘을 이용한다.
# 시간복잡도는 간선들을 정렬하는 시간에 좌우되기 때문에 O(ElogE)이다.

# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
# 2-1. 사이클이 발생하지 않는 경우, 최소 신장 트리에 포함시킨다.
# 2-2. 사이클이 발생하는 경우, 최소 신장 트리에 포함시키지 않는다.
# -> 모든 간선에 대해 반복한다.
# 노드들 간의 사이클이 발생하는지 여부는 union-find 연산에서 간선을 확인하며 두 노드의 부모 노드를 확인한다.
# 노드들의 부모노드가 같다면 사이클이 발생, 같지 않다면 사이클이 발생하지 않음을 의미

# 특정 원소가 속한 집합 찾기
# 부모노드 찾기
def find(parent, x):
    # 자기자신이 부모노드인 노드가 나올 때까지
    if parent[x] != x: # 자기 자신이 부모노드가 아니라면
        parent[x] = find(parent, parent[x]) # 부모노드의 부모노드도 확인

    # 최종 저장된 부모노드 반환
    return parent[x]

# 두 원소가 속한 집합 합치기
# 최소 신장 트리에 포함시키기
def union(parent, a, b):
    rootA = find(parent, a) # 노드 a의 부모 노드
    rootB = find(parent, b) # 노드 b의 부모 노드

    # 더 작은 숫자를 가진 부모노드로 합치기
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

# kruskal 알고리즘
def kruskal():
    result = 0 # 최소 비용 결과 값 저장할 변수

    # 모든 간선에 대해
    for edge in edges:
        cost, a, b = edge
        # 두 노드의 부모 노드가 다르다면 사이클이 발생하지 않는 것이므로
        if find(parent, a) != find(parent, b): # 다르다면
            union(parent, a, b) # 최소 신장 트리에 간선 포함시키기
            result += cost # 최소 비용 결과 값에 간선 비용 더하기
    
    return result

# 노드, 간선 개수 입력 받기
v, e = map(int, input().split())

# Union-Find 연산을 위한 부모 테이블 생성 & 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i # 자기 자신으로 초기화

# 간선에 대한 정보를 담는 리스트
edges = []
for i in range(e):
    v1, v2, cost = map(int, input().split()) # 정점1, 정점2, 가중치
    edges.append((cost, v1, v2)) # 간선 비용을 기준으로 정렬하기 위해 간선을 맨 앞에 저장

edges.sort() # 간선 비용을 기준으로 오름차순 정렬

print(kruskal())