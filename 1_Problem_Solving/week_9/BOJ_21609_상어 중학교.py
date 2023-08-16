from collections import deque

# 인접 블록 찾기 -> 블록 크기, 무지개 크기, 블록 좌표 리턴
def bfs(x, y, color):
    queue = deque()
    queue.append((x, y))
    blockCount, rainbowCount = 1, 0 # 블록 개수, 무지개 블록 개수
    blocks = [(x, y)] # 블록 좌표 넣을 리스트
    rainbows = [] # 무지개 좌표 넣을 리스트

    while queue:
        curx, cury = queue.popleft()

        for i in range(4):
            nextx = curx + dx[i]
            nexty = cury + dy[i]

            # 범위 안이면서 방문하지 않은 일반 블록인 경우
            if 0 <= nextx < n and 0 <= nexty < n and not visited[nextx][nexty] and game[nextx][nexty] == color:
                blockCount += 1
                visited[nextx][nexty] = 1
                queue.append((nextx, nexty))
                blocks.append((nextx, nexty))
            # 범위 안이면서 방문하지 않은 무지개 블록인 경우
            elif 0 <= nextx < n and 0 <= nexty < n and not visited[nextx][nexty] and game[nextx][nexty] == 0:
                blockCount += 1
                rainbowCount += 1
                visited[nextx][nexty] = 1
                queue.append((nextx, nexty))
                rainbows.append((nextx, nexty))

    # 무지개 블록은 방문 다시 해제 (다른 블록 그룹과 겹칠 수 있기 때문에)
    for x, y in rainbows:
        visited[x][y] = 0

    return [blockCount, rainbowCount, blocks+rainbows]

# 블록 제거 함수
def remove(block):
    for x, y in block:
        game[x][y] = -2

# 중력 함수
def gravity(game):
    for i in range(n-2, -1, -1): # 밑에서부터 체크
        for j in range(n):
            if game[i][j] > -1: # 검정(-1)이 아니라면
                r = i
                while True:
                    if 0 <= r+1 < n and game[r+1][j] == -2: # 다음 행이 범위 안이면서 -2이면
                        game[r+1][j] = game[r][j] # 아래로 다운
                        game[r][j] = -2
                        r += 1
                    else:
                        break

# 반시계로 90도 회전 함수
def rotate(game):
    newGame = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newGame[n-1-j][i] = game[i][j]
    return newGame

# 메인
n, m = map(int, input().split())
game = []
for _ in range(n):
    game.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
score = 0

# 1. 오토플레이
# -> while{
# 2. 크기 가장 큰 블록 찾기 
# 3. 블록제거 + 점수 더하기 
# 4. 중력 
# 5. 90도 회전 
# 6. 중력}
while True:
    # 2. 크기 가장 큰 블록 찾기
    visited = [[0] * n for _ in range(n)]
    blocks = [] # 가능한 블록 그룹들 넣을 리스트
    for i in range(n):
        for j in range(n):
            if game[i][j] > 0 and not visited[i][j]: # 일반 블록이면서 방문하지 않았으면
                visited[i][j] = 1 # 방문 처리
                blockInfo = bfs(i, j, game[i][j]) # 인접 블록 찾기
                # blockInfo = [블록크기, 무지개블록 개수, 블록좌표] 로 리턴되어 저장
                if blockInfo[0] >= 2:
                    blocks.append(blockInfo)
    blocks.sort(reverse=True) # 블록 그룹 크기 오름차순으로 정렬

    # 3. 블록제거 + 점수 더하기
    if not blocks:
        break
    remove(blocks[0][2])
    score += blocks[0][0] ** 2

    # 4. 중력
    gravity(game)

    # 5. 90도 회전
    game = rotate(game)

    # 6. 중력
    gravity(game)

print(score)