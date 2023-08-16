n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

# 북(0) 동(1) 남(2) 서(3) 방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 방문 확인 리스트
visited = [[0] * m for _ in range(n)]

# 처음 시작하는 곳 방문 처리하고 청소한 칸 개수 1 증가
visited[r][c] = 1
count = 1

while True:
    available = 0 # 주변 4칸 중 청소 가능한 칸이 있는지 저장

    # 주변 4칸 다 확인
    for _ in range(4):
        d = (d+3)%4 # 반시계 방향으로 90도 돌린다
        # 돌린 방향으로 한 칸 전진한 위치
        nr = r + dr[d]
        nc = c + dc[d]

        # 그 위치가 범위 안에 들고, 빈 칸이고, 청소할 수 있다면
        if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1 # 방문 처리
                count += 1 # 청소한 칸 개수 1 증가
                r, c = nr, nc # 위치 이동
                available = 1 # 청소 가능한 칸이 있어 청소했음 표시
                break
    
    # 주변 4칸 중 청소 가능한 칸이 없을 때
    if available == 0:
        if room[r-dr[d]][c-dc[d]] == 1: # 후진했을 때 벽이라면
            print(count) # 출력하고
            break # 작동 멈춤
        else: # 후진 가능하다면
            r, c = r-dr[d], c-dc[d] # 후진하고 계속
