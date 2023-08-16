from collections import deque

# 최단 거리, 최단 횟수, 최단 경로를 구하는 경우 -> BFS 사용
# optimal한 답을 찾는 경우, 가장 처음 발견되는 해답이 최단 거리
def bfs(x, y):
    queue = deque()

    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 상하좌우로 이동해 탐색
        for i in range(4):
            nx = x + dx[i] # 이동할 칸의 행 값
            ny = y + dy[i] # 이동할 칸의 열 값
            if 0 <= nx < n and 0 <= ny < m: # 미로의 범위를 벗어나지 않으면서
                if maze[nx][ny] == 1: # 이동할 수 있는 칸이라면
                    queue.append((nx, ny)) # 큐에 삽입
                    # DP와 같이 그래프의 값 자체를 이동 횟수로 저장하면서 탐색 진행
                    maze[nx][ny] = maze[x][y] + 1
    
    return maze[n-1][m-1]



n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

# 상하좌우 방향 배열
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(bfs(0, 0))