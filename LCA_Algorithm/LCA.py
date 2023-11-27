# Lowest Common Ancestor (LCA; 최소 공통 조상) Algorithm
# 트리 그래프에서 임의의 두 노드 A, B가 주어졌을 때,
# 정점 A와 정점 B가 각각 자신을 포함하여 조상을 따라 거슬러 올라 갈 때 처음 공통으로 만나게 되는 정점이다.
# 정점 A 혹은 A의 조상이면서 정점 B 혹은 B의 조상인 정점들 중 깊이가 가장 깊은 정점이다.
# 1. 모든 노드들에 대한 깊이를 계산한다.
# 2. 최소 공통 조상을 찾을 두 노드를 확인한다.
# 3. 두 노드의 깊이가 동일하도록 거슬러 올라간다.
# 4. 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라간다.
# 5. 모든 LCA(a, b) 연산에 대해 3~4번의 과정을 반복한다.


# 기본적인 LCA 알고리즘
# 최악의 경우, O(N)의 시간복잡도를 가진다.
import sys

input = sys.stdin.readline()
sys.setrecursionlimit(int(1e5))  # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정


# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, deep):
    calculated[x] = True
    depth[x] = deep
    for y in graph[x]:
        if calculated[y]:  # 이미 깊이를 구했다면 넘어간다.
            continue
        parent[y] = x
        dfs(y, deep + 1)


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


n = int(input())  # 노드 개수
parent = [0] * (n + 1)  # 부모 노드 정보
depth = [0] * (n + 1)  # 각 노드까지의 깊이
calculated = [0] * (n + 1)  # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)]  # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)  # 루트 노드가 1번일 경우
a, b = map(int, input().split())
print(lca(a, b))


# 개선된 LCA 알고리즘
# Dynamic Programming을 이용해 시간 복잡도를 개선할 수 있다.
# 모든 노드에 대하여 각 노드의 부모뿐 아니라 2^k번째 조상까지 저장한다.
# O(logN)의 시간복잡도를 가진다.
# 예시) 백준 11438번 LCA2 문제
import sys

input = sys.stdin.readline()
sys.setrecursionlimit(int(1e5))  # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정

LOG = 21  # 2^20 = 1,000,000


# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, deep):
    calculated[x] = True
    depth[x] = deep
    for y in graph[x]:
        if calculated[y]:
            continue
        parent[y][0] = x
        dfs(y, deep + 1)


# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1, 0)  # 루트 노드가 1번 노드일 경우
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]


# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # b가 더 깊도록 설정
    if depth[a] > depth[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]


n = int(input())
parent = [[0] * LOG for _ in range(n + 1)]  # 부모 노드 정보
depth = [0] * (n + 1)  # 각 노드까지의 깊이
calculated = [0] * (n + 1)  # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)]  # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()
a, b = map(int, input().split())
print(lca(a, b))
