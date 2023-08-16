from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

# 어디에 벽을 세워야 최댓값이 나올지 알 수 없기 때문에 벽을 세울 수 있는 모든 경우의 수에 대해 수행해 봐야 한다.
# 1. 벽 3개를 선택해서 다른 배열에 복사
# 2. 바이러스는 상하좌우의 인접한 빈 칸으로 이동하므로 BFS 수행
# 2-1. 바이러스의 위치를 큐에 전부 넣고 while 문 돌린다.
# 2-2. 바이러스가 퍼져 나간 후 빈 칸(0)이 몇 개 있는지 체크
# 3. 최댓값을 찾는다.
# 4. 선택한 벽 3개를 지운다. -> 1번으로 가서 반복


# 방법 1 => python3으로 제출하면 시간 초과
# 3개의 벽을 세운 후 퍼져 나가는 바이러스의 수를 구함
def bfsVirus():
    global result
    queue = deque()
    tempLab = copy.deepcopy(lab) # deepcopy로 벽이 선택된 배열 복사해 임시 배열에 저장

    for i in range(n):
        for j in range(m):
            if tempLab[i][j] == 2: # 임시 배열에서 바이러스를 발견하면
                queue.append((i, j)) # 큐에 삽입

    while queue:
        x, y = queue.popleft()

        # 상하좌우로 이동해 탐색
        for i in range(4):
            nx = x + dx[i] # 이동할 칸의 행 값
            ny = y + dy[i] # 이동할 칸의 열 값

            if 0 <= nx < n and 0 <= ny < m: # 지도의 범위를 벗어나지 않으면서
                if tempLab[nx][ny] == 0: # 빈 칸이라면
                    tempLab[nx][ny] = 2 # 바이러스 퍼짐
                    queue.append((nx, ny))
    
    # 바이러스가 모두 퍼져 나간 후에는,
    count = 0
    for i in range(n):
        # 남아 있는 빈 칸(안전 영역) 개수 구함
        count += tempLab[i].count(0)

    # 안전 영역 크기의 최댓값 저장
    result = max(result, count)

# 새로 세울 3개의 벽을 선택
def makeWall(count):
    if count == 3: # 벽 3개가 선택되면
        bfsVirus() # 바이러스 퍼뜨리기
        return
    
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0: # 빈 칸인 경우
                lab[i][j] = 1 # 벽으로 변경
                makeWall(count + 1) # 벽으로 선택
                lab[i][j] = 0 # BFS 수행 후 다시 빈 칸으로 변경


# 방법 2 => 시간 초과 나지 않음 => combinations 사용
def dfsCombi():
    global result

    # 새로 세울 벽 3개의 모든 조합 얻기
    for wall in combinations(empty, 3):
        tempLab = copy.deepcopy(lab) # deepcopy로 벽이 선택된 배열 복사해 임시 배열에 저장
        for x, y in wall:
            tempLab[x][y] = 1 # 조합에 따라 벽 생성

        virus = []
        for i in range(n):
            for j in range(m):
                if lab[i][j] == 2:
                    virus.append((i, j)) # 바이러스 위치

        # 바이러스가 다 퍼질 때까지
        while virus:
            x, y = virus.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 지도의 범위를 벗어나지 않으면서, 빈 칸이라면
                if 0 <= nx < n and 0 <= ny < m and tempLab[nx][ny] == 0:
                    tempLab[nx][ny] = 2 # 바이러스 퍼짐
                    virus.append((nx, ny)) # 바이러스 퍼짐
        
        # 바이러스가 모두 퍼져 나간 후에는,
        count = 0
        for row in tempLab:
            # 남아 있는 빈 칸(안전 영역) 개수 구함
            count += row.count(0)
        
        # 안전 영역 크기의 최댓값 저장
        result = max(result, count)


n, m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

# 상하좌우 방향 배열
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0

# 방법 1
# makeWall(0)

# 방법 2
empty = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i, j)) # 빈 칸 위치

dfsCombi()

# 결과 출력
print(result)