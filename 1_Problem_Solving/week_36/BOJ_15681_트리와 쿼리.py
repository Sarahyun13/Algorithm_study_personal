import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def dfs(node):
    visited[node] = 1  # 자기 자신 추가
    for next in tree[node]:
        if not visited[next]:  # 아직 방문하지 않은 노드가 있다면
            visited[node] += dfs(next)  # 방문하며 그 노드의 서브 트리 정점 개수를 더해준다.

    return visited[node]  # 서브트리에 속한 정점의 개수를 리턴한다.


N, R, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [0] * (N + 1)
dfs(R)
for _ in range(Q):
    u = int(input())
    print(visited[u])
