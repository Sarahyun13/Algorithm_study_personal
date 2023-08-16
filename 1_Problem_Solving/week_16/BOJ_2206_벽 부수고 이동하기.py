from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    visited[x][y][z] = 1

    while queue:
        x, y, z = queue.popleft()

        # 도착지점에 도착하면 최단 거리 출력
        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 다음 이동할 곳이 벽이고, 벽을 부술 기회가 남았다면
                if graph[nx][ny] == 1 and z == 0:
                    queue.append((nx, ny, 1))  # 벽을 부수고 큐에 저장
                    visited[nx][ny][1] = visited[x][y][0] + 1
                # 다음 이동할 곳이 벽이 아니고, 방문한 적도 없다면
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    queue.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1

    return -1


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 3차원 리스트 visited[x][y][z]로 벽 부숨 유무 기록
# z == 0 이면 벽을 부수지 않은 경우, z == 1 이면 벽을 부순 경우
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
print(bfs(0, 0, 0))
