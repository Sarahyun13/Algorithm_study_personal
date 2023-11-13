import sys

input = sys.stdin.readline


# dfs 사용해서 탐색
def dfs(node, count):
    visited[node] = 1

    for next in planes[node]:
        if not visited[next]:
            count = dfs(next, count + 1)

    return count


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    planes = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        planes[a].append(b)
        planes[b].append(a)

    visited = [0] * (N + 1)
    print(dfs(1, 0))


# 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.
# -> 답은 무조건 N-1
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     for _ in range(M):
#         a, b = map(int, input().split())
#     print(N-1)
