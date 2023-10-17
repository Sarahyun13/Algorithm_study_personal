# Python3로 돌리면 시간 초과 남
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2):
        x, y = i, i
        temp = array[x][y]

        # 좌
        for j in range(i + 1, N - i):
            x = j
            preVal = array[x][y]
            array[x][y] = temp
            temp = preVal

        # 하
        for j in range(i + 1, M - i):
            y = j
            preVal = array[x][y]
            array[x][y] = temp
            temp = preVal

        # 우
        for j in range(N - i - 2, i - 1, -1):
            x = j
            preVal = array[x][y]
            array[x][y] = temp
            temp = preVal

        # 상
        for j in range(M - i - 2, i - 1, -1):
            y = j
            preVal = array[x][y]
            array[x][y] = temp
            temp = preVal

for row in array:
    print(*row)
