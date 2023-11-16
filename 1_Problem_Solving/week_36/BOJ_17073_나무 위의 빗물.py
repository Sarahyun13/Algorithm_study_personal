import sys

input = sys.stdin.readline


def dfs(node):
    stack = [node]
    visited[node] = True
    leaf = 0

    while stack:
        now = stack.pop()
        if len(tree[now]) == 1 and visited[tree[now][0]]:
            leaf += 1
        for next in tree[now]:
            if not visited[next]:
                visited[next] = True
                stack.append(next)

    return leaf


N, W = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (N + 1)
leaf = dfs(1)
print(W / leaf)
