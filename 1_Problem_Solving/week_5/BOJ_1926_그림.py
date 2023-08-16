from collections import deque

# 1. BFS
def bfs(x, y):
    queue = deque() # 큐 생성

    queue.append((x, y))
    count = 1 # 처음 들어온 위치는 그림이므로 넓이에 1 저장
    visit[x][y] = True # 방문 처리

    while queue:
        x, y = queue.popleft()

        # 상하좌우로 이동해 탐색
        for i in range(4):
            nx = x + dx[i] # 이동할 칸의 행 값
            ny = y + dy[i] # 이동할 칸의 열 값

            if 0 <= nx < n and 0 <= ny < m: # 도화지의 범위를 벗어나지 않으면서
                if visit[nx][ny] == False and draw[nx][ny] == 1: # 방문하지 않았고, 1의 값을 가진 그림이라면
                    count += 1 # 넓이 1 증가
                    visit[nx][ny] = True # 방문 처리
                    queue.append((nx, ny)) # 큐에 삽입

    return count

# 2. DFS
def dfs(x, y):
    stack = list() # 스택 생성

    stack.append((x, y))
    count = 1
    visit[x][y] = True

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == False and draw[nx][ny] == 1:
                    count += 1
                    visit[nx][ny] = True
                    stack.append((nx, ny))
    
    return count

n, m = map(int, input().split())
draw = []
for _ in range(n):
    draw.append(list(map(int, input().split())))

visit = [[False] * m for _ in range(n)] # 방문 여부 배열
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1] # 상하좌우 방향 배열
result = [] # 그림 크기 저장 배열

for x in range(n):
    for y in range(m):
        # 현재 위치에 있는 값이 1이라 그림이고, 방문하지 않았다면
        if draw[x][y] == 1 and visit[x][y] == False:
            #result.append(bfs(x, y)) # bfs로 방문
            result.append(dfs(x, y)) # dfs로 방문

print(len(result)) # 그림의 개수 출력
if len(result) == 0: # 그림이 하나도 없는 경우
    print(0) # 가장 넓은 그림의 넓이는 0
else: # 그림이 하나라도 있는 경우
    print(max(result)) # 모든 그림들 중 가장 넓은 그림의 넓이 출력