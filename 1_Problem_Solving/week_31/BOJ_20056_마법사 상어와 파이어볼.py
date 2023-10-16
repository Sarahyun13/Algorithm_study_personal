import sys

input = sys.stdin.readline

# N: 행/열 크기, M: 파이어볼 갯수, K: 이동 횟수
N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
fireballs = []
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(M):
    row, col, mass, speed, direction = map(int, input().split())
    fireballs.append([row - 1, col - 1, mass, speed, direction])

for _ in range(K):
    # 파이어볼 이동
    while fireballs:
        r, c, m, s, d = fireballs.pop(0)
        nr = (r + dx[d] * s) % N
        nc = (c + dy[d] * s) % N
        graph[nr][nc].append([m, s, d])

    for x in range(N):
        for y in range(N):
            if len(graph[x][y]) > 1:  # 2개 이상이라면 합쳐진 후, 4개로 나누어진다
                mSum, sSum, odd, even, count = 0, 0, 0, 0, len(graph[x][y])
                while graph[x][y]:
                    m, s, d = graph[x][y].pop(0)
                    mSum += m
                    sSum += s
                    if d % 2 == 0:
                        even += 1
                    else:
                        odd += 1

                if even == count or odd == count:  # 방향이 모두 홀수이거나 모두 짝수라면
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if mSum // 5:  # 질량이 0이 아니라면 파이어볼 리스트에 추가, 0이라면 소멸
                    for d in nd:
                        fireballs.append([x, y, mSum // 5, sSum // count, d])

            if len(graph[x][y]) == 1:  # 1개만 있다면 그대로 파이어볼 리스트에 추가
                fireballs.append([x, y] + graph[x][y].pop())

# print(fireballs)
total = 0
for fireball in fireballs:
    total += fireball[2]
print(total)
