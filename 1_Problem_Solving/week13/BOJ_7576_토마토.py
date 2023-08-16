from collections import deque
import sys

input = sys.stdin.readline


# bfs 함수 안에서는 바로 시작
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                queue.append((nx, ny))
                # 익히고 1을 더해주면서 횟수 세어주기
                # 여기서 나온 제일 큰 값이 정답
                tomato[nx][ny] = tomato[x][y] + 1


M, N = map(int, input().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int, input().split())))

# 최소 시간
# -> 한 번에 여러 곳을 동시에 확인해야 하므로 큐를 바깥에 생성,
#    익은 토마토 미리 다 큐에 삽입
queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

bfs()

result = 0
for row in tomato:
    for col in row:
        if col == 0:
            print(-1)  # 토마토를 다 익히지 못했다면 -1 출력
            exit(0)  # 종료
    # 다 익혔다면 최댓값이 정답
    result = max(result, max(row))

# 처음 시작을 1로 나타냈으니 결과에는 1을 빼줌
print(result - 1)
