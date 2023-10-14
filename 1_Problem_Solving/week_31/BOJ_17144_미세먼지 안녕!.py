import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

# 모든 미세먼지의 확산이 동시에 일어나므로 값 변환 저장할 temp 배열 생성
temp = [[0] * C for _ in range(R)]
for _ in range(T):
    for x in range(R):
        for y in range(C):
            temp[x][y] = room[x][y]

    # 미세먼지가 인접한 네 방향으로 확산
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(R):
        for y in range(C):
            if room[x][y] > 0:
                dust = room[x][y] // 5
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] >= 0:
                        temp[nx][ny] += dust
                        temp[x][y] -= dust

    # 공기청정기 위치 구함과 동시에 확산된 미세먼지 배열 복사
    airx1, airy1, airx2, airy2 = 0, 0, 0, 0
    for x in range(R):
        for y in range(C):
            room[x][y] = temp[x][y]
            if temp[x][y] == -1 and not airx1:
                airx1 = x
            elif temp[x][y] == -1 and not airx2:
                airx2 = x
    # print(room)

    # 위쪽 공기청정기에 의한 미세먼지 이동
    for x in range(airx1 - 2, -1, -1):
        room[x + 1][0] = room[x][0]
    for y in range(1, C):
        room[0][y - 1] = room[0][y]
    for x in range(1, airx1 + 1):
        room[x - 1][C - 1] = room[x][C - 1]
    for y in range(C - 2, 0, -1):
        room[airx1][y + 1] = room[airx1][y]

    # 아래쪽 공기청정기에 의한 미세먼지 이동
    for x in range(airx2 + 2, R):
        room[x - 1][0] = room[x][0]
    for y in range(1, C):
        room[R - 1][y - 1] = room[R - 1][y]
    for x in range(R - 2, airx2 - 1, -1):
        room[x + 1][C - 1] = room[x][C - 1]
    for y in range(C - 2, 0, -1):
        room[airx2][y + 1] = room[airx2][y]

    # 공기청정기 옆 칸 0으로 초기화
    room[airx1][1], room[airx2][1] = 0, 0

dustSum = 0
for row in room:
    # print(*row)
    dustSum += sum(row)

print(dustSum + 2)
