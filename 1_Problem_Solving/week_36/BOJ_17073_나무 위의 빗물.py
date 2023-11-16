import sys

input = sys.stdin.readline

# '물의 양 / 리프 노드 개수' 를 구하면 된다.


def dfs(node):
    stack = [node]
    visited[node] = True
    leaf = 0

    while stack:
        now = stack.pop()
        # 연결된 노드가 1개이고, 그 하나가 부모노드라면 리프 노드이므로 리프 노드 개수 증가시킴
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
