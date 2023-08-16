# DFS와 DP를 이용하는 문제
# import sys
# sys.setrecursionlimit(10**9) # 재귀에서 RecursionError 방지를 위해

def dfs(x, y):
    # 오른쪽 맨 밑에 도착하면 1을 반환해 끝까지 이동한 모든 칸에 1을 더한다.
    if x == m-1 and y == n-1:
        return 1
    
    if dp[x][y] == -1: # 아직 탐색하지 않은 칸이라면
        dp[x][y] = 0 # 탐색한다는 의미의 0 저장
        # 방향 배열 이용해서 현재 칸의 상하좌우로 이동해 탐색
        for i in range(4):
            nx = x + dx[i] # 이동할 칸의 행 값
            ny = y + dy[i] # 이동할 칸의 열 값
            if 0 <= nx < m and 0 <= ny < n: # 지도의 범위를 벗어나지 않으면서
                if mapArr[nx][ny] < mapArr[x][y]: # 현재 칸보다 높이가 낮다면
                    # nx, ny 방향으로 탐색 시작(재귀호출)
                    # x, y 위치에서부터 목적지까지 갈 수 있는 경우의 수를 dp[x][y]에 저장
                    dp[x][y] += dfs(nx, ny)
    
    # 탐색한 칸이거나 탐색할 수 없는 칸이라면 그대로 리턴
    # 마지막에는 시작 칸 dp[0, 0]을 리턴
    return dp[x][y]

m , n = map(int, input().split())
mapArr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)] # 아직 탐색하지 않았다는 의미의 -1로 전체 초기화
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1] # 상하좌우 방향 배열

print(dfs(0, 0))
