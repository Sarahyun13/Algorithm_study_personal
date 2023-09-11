import sys

input = sys.stdin.readline


# 친구 관계를 그래프로 표현한다면, 문제에서 요구하는 조건은 a-b-c-d-e 그래프가 있어야 한다는 것이다.
# 탐색하며 해당 그래프의 깊이가 5임을 증명하면 된다.
def dfs(idx, depth):
    if depth == 4:
        print(1)
        exit()

    for i in rel[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False


N, M = map(int, input().split())
rel = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
