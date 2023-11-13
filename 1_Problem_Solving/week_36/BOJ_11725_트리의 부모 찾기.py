import sys

input = sys.stdin.readline


# 루트 노드인 1부터 dfs로 탐색을 시작하면 부모 -> 자식으로만 이동
def dfs(node, visited):
    stack = [node]
    visited[node] = 1

    while stack:
        now = stack.pop()
        for next in tree[now]:
            if not visited[next]:
                visited[next] = now
                stack.append(next)


N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (N + 1)
dfs(1, visited)

for i in range(2, N + 1):
    print(visited[i])
