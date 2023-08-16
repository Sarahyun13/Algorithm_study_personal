from collections import deque
import sys

input = sys.stdin.readline


# 섬 구분
def divideBfs(x, y):
    global islandNum

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    graph[x][y] = islandNum

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and graph[nx][ny] == 1
                and not visited[nx][ny]
            ):
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = islandNum


# 최단 다리 길이
def bridgeBfs(v):
    global answer

    dist = [[-1] * N for _ in range(N)]  # 거리가 저장될 리스트
    queue = deque()

    # 같은 번호인 섬의 육지 부분을 모두 큐에 삽입
    for i in range(N):
        for j in range(N):
            if graph[i][j] == v:
                queue.append((i, j))
                dist[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 다른 땅을 만나면 기존에 저장된 값과 비교하여 짧은 거리 선택
                if graph[nx][ny] > 0 and graph[nx][ny] != v:
                    answer = min(answer, dist[x][y])
                    return
                # 바다를 만나면 dist 값을 1씩 증가시킴
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * N for _ in range(N)]
islandNum = 1

# 섬 번호로 구분 짓기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            divideBfs(i, j)
            islandNum += 1

# print(graph)

answer = 1e9
# 최단 다리 길이 찾기
for i in range(1, islandNum):
    bridgeBfs(i)

print(answer)
