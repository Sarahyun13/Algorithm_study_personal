import sys

input = sys.stdin.readline

N = int(input())
target = int(input())

board = [[0] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1  # 같은 방향에서 몇 개를 채우는지 저장하는 변수
di = 0
x, y = N // 2, N // 2
n = 1
board[x][y] = n  # 첫 시작
n += 1
while count <= N - 1:
    if count < N - 1:
        iterNum = 2  # 방향 변경은 2번씩 반복됨
    elif count == N - 1:
        iterNum = 3  # 마지막 방향 변경은 3번 반복됨
    for _ in range(iterNum):  # iterNum만큼 방향 변경
        for _ in range(count):  # 같은 방향으로 count만큼 표 채움
            x += dx[di]  # 방향 변경
            y += dy[di]  # 방향 변경
            board[x][y] = n
            n += 1
        di = (di + 1) % 4  # 다음 방향 좌표 대입
    count += 1  # iterNum(2번) 방향을 바꿨다면 1 증가시킴

answer = []
ansx, ansy = None, None
for i in range(N):
    for j in range(N):
        print(board[i][j], end=" ")

        if board[i][j] == target:
            ansx = i + 1
            ansy = j + 1
    print()

print(ansx, ansy)
