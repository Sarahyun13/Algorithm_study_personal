import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y, count):
    visited[x][y] = count  # 그룹 넘버 부여
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 아직 그룹화 되지 않은 '1'이라면
                if not visited[nx][ny] and array[nx][ny]:
                    visited[nx][ny] = count  # 그룹 넘버 부여
                    queue.append((nx, ny))


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * M for _ in range(N)]

# visited의 숫자에 따라 영역 구별하기 ('1' 그룹화 시키기)
count = 1  # 그룹 넘버
for x in range(N):
    for y in range(M):
        if array[x][y] and not visited[x][y]:
            bfs(x, y, count)
            count += 1  # 그룹 넘버 1 증가시킴

# dic에 영역(그룹)별(key)로 영역(그룹)의 크기(value)를 지정
group = dict()
for x in range(N):
    for y in range(M):
        if not visited[x][y] in group:  # group 딕셔너리에 존재하지 않는 그룹이라면
            group[visited[x][y]] = 1  # 새로 추가
        else:  # 이미 존재하는 그룹이라면
            group[visited[x][y]] += 1  # 크기 늘림

# 배열의 0인 부분만 보고 상하좌우를 체크, 영역(그룹)별 최대 크기를 초기화 해 준다.
result = 0  # 최종 결과 값 저장할 변수
for x in range(N):
    for y in range(M):
        if array[x][y] == 0:  # 0이라면
            groupSet = set()  # 0이 1로 변경됐을 경우, 포함될 수 있는 주변 그룹을 저장할 set(중복 제거를 위해)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    # 배열 값이 1이고, 그룹화 되어있다면
                    if array[nx][ny] == 1 and visited[nx][ny] != 0:
                        groupSet.add(visited[nx][ny])  # 그룹셋에 추가

            # 0을 1로 하나씩 바꾸고 그룹 저장할 때마다 큰 결과 값으로 갱신
            # 바꾼 0의 주변 그룹이 여러 개라면 그 0이 1로 바뀜으로 인해서 주변 그룹이 다 연결되므로
            # 그룹셋에 저장된 그룹 크기 다 더함
            tempRes = 0
            for s in groupSet:
                tempRes += group[s]

            # 저장된 그룹과 새 그룹 크기 비교 후, 더 큰 값 저장
            result = max(result, tempRes + 1)

print(result)
