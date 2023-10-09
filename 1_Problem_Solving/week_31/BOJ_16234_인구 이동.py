import sys
from collections import deque

input = sys.stdin.readline


# BFS 이용해서 연합국 그룹핑
def bfs_grouping(x, y, num):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == 0:
                if L <= abs(country[x][y] - country[nx][ny]) <= R:  # 연합 가능하다면
                    # 그룹 넘버 대입해서 연합
                    union[x][y] = num
                    union[nx][ny] = num
                    # 그룹 set에도 인덱스 추가
                    groupSet.add((x, y))
                    groupSet.add((nx, ny))
                    queue.append((nx, ny))


N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0  # 인구이동 수행 횟수
while True:
    union = [[0] * N for _ in range(N)]  # 연합 상태 저장할 리스트
    num = 0
    groupDict = dict()  # 연합국 그룹 결과 담을 딕셔너리
    for x in range(N):
        for y in range(N):
            if union[x][y] == 0:  # 연합되지 않은 국가라면
                groupSet = set()  # 새로운 그룹set 생성
                num += 1
                bfs_grouping(x, y, num)  # 연합 그룹핑
                if groupSet:  # 어느 한 국가라도 연합된다면
                    groupDict[num] = list(
                        groupSet
                    )  # 딕셔너리에 저장 -> 그룹핑 넘버(key): 연합국들 인덱스 set(value)

    # 그룹핑 결과 아무것도 그룹핑 되지 않는다면
    # 열린 국경선이 없는 것이기 때문에 break
    unionSum = 0
    for row in union:
        unionSum += sum(row)
    if unionSum == 0:
        break

    # 국경선이 열려 있어 연합된(그룹핑 된) 국가들이 존재한다면
    count += 1  # 인구이동 횟수 증가
    for val in groupDict.values():  # 그룹(연합)별 인구 이동
        groupSum = 0  # 연합의 인구 수 저장할 변수
        for i in range(len(val)):  # 저장한 인덱스로 접근해
            groupSum += country[val[i][0]][val[i][1]]  # 그룹 인구 수 더하기
        avg = groupSum // len(val)  # 연합 인구의 평균

        for i in range(len(val)):  # 다시 저장한 인덱스로 접근해
            country[val[i][0]][val[i][1]] = avg  # 연합 인구 평균으로 인구 수 수정

    # print(union)
    # print(groupDict)
    # print(country)

print(count)
