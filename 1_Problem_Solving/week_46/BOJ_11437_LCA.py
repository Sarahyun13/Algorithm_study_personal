# pypy3로 제출해야 함.
# python3는 시간 초과
import sys
sys.setrecursionlimit(10**5) # 런타임 에러(RecursionError) 방지

input = sys.stdin.readline

# 루트 노드부터의 깊이 구하기
def dfs(x, d):
    visited[x] = True
    depth[x] = d

    # 현재 노드와 연결되어 있는 노드 확인
    for next in graph[x]:
        if not visited[next]: # 아직 탐색하지 않은 노드라면
            parent[next] = x # 부모 노드에 현재 노드 삽입
            dfs(next, d+1)

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이(depth)가 동일하도록
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1) # 각 노드의 부모 노드 정보
depth = [0] * (N+1) # 각 노드까지의 깊이
visited = [0] * (N+1) # 방문 여부

# 루트 노드부터 연결된 노드를 탐색
dfs(1, 0)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))