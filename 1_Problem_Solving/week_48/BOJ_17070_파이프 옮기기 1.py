import sys

input = sys.stdin.readline

# dir(방향) => 0: 가로, 1: 세로, 2: 대각선
N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

# 1. DFS 방법 => python3로 제출하면 시간 초과, pypy3로 제출해야 함.
def dfs(dir, x, y):
    global count

    if x == N-1 and y == N-1:
        count += 1
        return

    # 가로로 가는 경우
    if dir == 0 or dir == 2: # 가로, 대각선 상태에서만 가능
        if y+1 < N and not house[x][y+1]:
            dfs(0, x, y+1)
    # 세로로 가는 경우
    if dir == 1 or dir == 2: # 세로, 대각선 상태에서만 가능
        if x+1 < N and not house[x+1][y]:
            dfs(1, x+1, y)
    # 대각선으로 가는 경우
    if dir == 0 or dir == 1 or dir == 2: # 모든 상태에서 가능
        if x+1 < N and y+1 < N and not house[x+1][y+1] and not house[x][y+1] and not house[x+1][y]:
            dfs(2, x+1, y+1)


count = 0
dfs(0, 0, 1)
print(count)

# 2. DP 방법
def dp_solve():
    # 초기값 설정
    dp[0][0][1] = 1 # 1행은 가로만 입력
    # 벽을 만나기 전까지 1로 넣어준다. 벽이 있으면 이후 값들은 0
    for i in range(2, N):
        if house[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]

    for i in range(1, N):
        for j in range(1, N):
            # 대각선으로 가는 경우
            if not house[i][j] and not house[i][j-1] and not house[i-1][j]:
                # 모든 상태에서 가능
                dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

            if house[i][j] == 0:
                # 가로로 가는 경우
                dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1] # 가로, 대각선 상태에서만 가능
                # 세로로 가는 경우
                dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j] # 세로, 대각선 상태에서만 가능

# 가로, 세로, 대각선 상태를 저장하기 위한 3차원 리스트
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
dp_solve()
print(sum(dp[i][N-1][N-1] for i in range(3)))