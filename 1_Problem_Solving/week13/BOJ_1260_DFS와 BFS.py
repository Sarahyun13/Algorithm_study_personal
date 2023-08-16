from collections import deque
import sys

input = sys.stdin.readline


def dfs(graph, v, visitDfs):
    visitDfs[v] = 1
    print(v, end=" ")

    for next in graph[v]:
        if visitDfs[next] == 0:
            dfs(graph, next, visitDfs)


def bfs(v):
    q = deque()
    q.append(v)
    visitBfs[v] = 1

    while q:
        cur = q.popleft()
        print(cur, end=" ")

        for next in graph[cur]:
            if visitBfs[next] == 0:
                visitBfs[next] = 1
                q.append(next)


N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    graph[v1].sort()
    graph[v2].sort()


visitBfs = [0] * (N + 1)
visitDfs = [0] * (N + 1)

dfs(graph, V, visitDfs)
print()
bfs(V)
