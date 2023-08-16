from collections import deque
import sys

input = sys.stdin.readline

# '#':벽, '.':지나갈 수 있는 공간, 'J':지훈의 시작 위치, 'F':불이 난 공간


def bfs():
    while queue:
        x, y = queue.popleft()
        # 현재 노드가 불이라면
        if visited[x][y] == "fire":
            count = "fire"
        # 현재 노드가 지훈이의 위치라면
        else:
            count = visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if visited[nx][ny] == -1 and (
                    graph[nx][ny] == "." or graph[nx][ny] == "@"
                ):
                    if count == "fire":
                        visited[nx][ny] = "fire"
                        queue.append((nx, ny))
                    else:
                        visited[nx][ny] = count + 1
                        queue.append((nx, ny))
            else:
                if count != "fire":
                    return count + 1

    return "IMPOSSIBLE"


R, C = map(int, input().split())
graph = []
visited = [[-1] * C for _ in range(R)]
queue = deque()
for i in range(R):
    graph.append(list(input().rstrip()))
    for j in range(C):
        if graph[i][j] == "J":
            start = (i, j)
            visited[i][j] = 0
        elif graph[i][j] == "F":
            visited[i][j] = "fire"
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue.append(start)
print(bfs())
