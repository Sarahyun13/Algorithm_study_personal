from collections import deque
import sys

input = sys.stdin.readline


# '.':빈 공간, '#':벽, '@':상근이의 시작 위치, '*':불
def bfs():
    # 큐에는 불의 위치와 상근이의 위치만 저장됨
    while queue:
        x, y = queue.popleft()

        # 현재 노드가 불이라면
        if visited[x][y] == "Fire":
            count = "Fire"
        # 현재 노드가 상근이라면
        else:
            count = visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 다음 노드가 범위 안이고,
            if 0 <= nx < h and 0 <= ny < w:
                # 방문한 적 없으면서 빈 공간이거나 상근이고,
                if visited[nx][ny] == -1 and (
                    graph[nx][ny] == "." or graph[nx][ny] == "@"
                ):
                    # 현재 노드가 불이라면
                    if count == "Fire":
                        # 다음 노드에 불이 번지므로 'Fire' 저장
                        visited[nx][ny] = count
                    # 현재 노드가 상근이라면
                    else:
                        # 상근이가 이동하므로 다음 노드에 현재 노드 + 1 저장
                        visited[nx][ny] = count + 1
                    queue.append((nx, ny))
            # 다음 노드가 범위 밖을 벗어나고,
            else:
                # 현재 노드가 불이 아니고 상근이라면
                if count != "Fire":
                    return count + 1  # 최종 시간 출력

    # 탈출할 수 없다면 불가능 출력
    return "IMPOSSIBLE"


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    graph = []
    visited = [[-1] * w for _ in range(h)]
    queue = deque()

    # 상근이는 불이 붙을 예정인 칸으로는 이동하지 못하므로 불을 이동시킨 후 상근이를 이동시킨다.
    # -> 이를 위해 큐에 불 위치 먼저 저장하고, 상근이 위치를 저장
    for i in range(h):
        graph.append(list(input().rstrip()))
        for j in range(w):
            # 상근이라면
            if graph[i][j] == "@":
                visited[i][j] = 0  # 0으로 업데이트
                start = (i, j)  # 상근이의 시작 위치를 변수에 저장
            # 불이라면
            elif graph[i][j] == "*":
                visited[i][j] = "Fire"  # Fire로 업데이트
                queue.append((i, j))  # 불 위치 큐에 저장

    queue.append(start)  # 변수에 저장해 둔 상근이의 위치를 큐에 저장
    print(bfs())
