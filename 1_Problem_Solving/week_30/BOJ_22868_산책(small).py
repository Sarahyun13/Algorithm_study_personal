import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, end, visited, startCount):
    queue = deque()
    queue.append((start, startCount))

    while queue:
        cur, cnt = queue.pop()

        # 목적지 end에 도달했을 때,
        if cur == end:
            # startCount가 0이라면 S->E의 경로를 구하는 것이므로
            # break로 빠져나와서 밑 while문으로 가서 경로 구함
            if startCount == 0:
                break
            # startCount에 길이를 전달 받았다면 E->S의 경로를 구하는 것이므로
            # 경로 길이 반환
            else:
                return cnt

        # 목적지 end가 아니라면
        # 연결된 노드들 확인
        for next in graph[cur]:
            if visited[next] == -1:
                visited[next] = cur
                queue.appendleft((next, cnt + 1))

    # visited 배열에 저장된 값들 거꾸로 찾아가 경로 반환
    route = [end]
    next = visited[end]
    while next != 0:
        route.append(next)
        next = visited[next]

    # 마지막 시작 노드 start 빼고 반환
    # (E->S 경로 구할 때 방문 처리에서 제외하기 위해서)
    return route[:-1]


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 사전순으로 경로를 나열하기 위해서 미리 정렬
for i in range(1, N + 1):
    graph[i].sort()

S, E = map(int, input().split())
# S -> E
visited = [-1] * (N + 1)
visited[S] = 0
# startCount 파라미터에 0 전달해서 S->E 경로를 구하는 것임을 표시
route = bfs(S, E, visited, 0)

# E -> S
visited = [-1] * (N + 1)
# S에서 E로 가면서 방문했던 곳들은 방문 처리
for i in route:
    visited[i] = 1
# startCount 파라미터에 len(route) 전달해서 E->S 경로를 구하는 것임을 표시
count = bfs(E, S, visited, len(route))

print(count)
