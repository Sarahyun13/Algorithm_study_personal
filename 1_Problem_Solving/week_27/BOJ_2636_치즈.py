import sys
from collections import deque

input = sys.stdin.readline


# 주어지는 판의 양끝 행과 열이 모두 비어있다는 것이 전제로 주어져 있다.
# 따라서, 처음 시작을 (0, 0)으로 하면 치즈 중간에 있는 구멍으로는 접근이 불가능하다.
# -> 신경쓰지 않아도 됨.
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 처리
                if cheese[nx][ny] == 1:  # 치즈라면
                    cheese[nx][ny] = 0  # 녹이고
                    count += 1  # 녹인 치즈 개수 증가시킴
                elif cheese[nx][ny] == 0:  # 공기라면
                    queue.append((nx, ny))  # 계속 탐색하기 위해 큐에 삽입

    result.append(count)
    return count


r, c = map(int, input().split())

cheese = []
for _ in range(r):
    cheese.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = []

# 치즈가 다 녹을 때까지 반복문 수행
time = 0
while True:
    time += 1
    visited = [[False] * c for _ in range(r)]
    count = bfs(0, 0)
    if count == 0:  # 치즈가 다 녹았다면
        break

print(time - 1)
print(result[-2])
