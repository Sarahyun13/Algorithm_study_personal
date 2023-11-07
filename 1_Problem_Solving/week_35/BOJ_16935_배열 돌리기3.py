import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

cal = list(map(int, input().split()))
for calNum in cal:
    if calNum == 1:  # 상하 반전
        # array = array[::-1]
        for r in range(N // 2):
            temp = array[r]
            array[r] = array[N - 1 - r]
            array[N - 1 - r] = temp
    elif calNum == 2:  # 좌우 반전
        # for r in range(N):
        #     array[r] = array[r][::-1]
        for r in range(N):
            for c in range(M // 2):
                temp = array[r][c]
                array[r][c] = array[r][M - 1 - c]
                array[r][M - 1 - c] = temp
    elif calNum == 3:  # 오른쪽으로 90도 회전
        temp = [[0] * N for _ in range(M)]
        for r in range(M):
            for c in range(N):
                temp[r][c] = array[N - 1 - c][r]
        array = temp
        N, M = M, N
    elif calNum == 4:  # 왼쪽으로 90도 회전
        temp = [[0] * N for _ in range(M)]
        for r in range(M):
            for c in range(N):
                temp[r][c] = array[c][M - 1 - r]
        array = temp
        N, M = M, N
    elif calNum == 5:  # 1 -> 2 -> 3 -> 4 -> 1
        temp = [[0] * M for _ in range(N)]
        # 1 -> 2
        for i in range(N // 2):
            for j in range(M // 2):
                temp[i][M // 2 + j] = array[i][j]

        # 2 -> 3
        for i in range(N // 2):
            for j in range(M // 2, M):
                temp[N // 2 + i][j] = array[i][j]

        # 3 -> 4
        for i in range(N // 2, N):
            for j in range(M // 2, M):
                temp[i][j - M // 2] = array[i][j]

        # 4 -> 1
        for i in range(N // 2, N):
            for j in range(M // 2):
                temp[i - N // 2][j] = array[i][j]

        array = temp

    elif calNum == 6:  # 4 -> 3 -> 2 -> 1 -> 4
        temp = [[0] * M for _ in range(N)]
        # 4 -> 3
        for i in range(N // 2, N):
            for j in range(M // 2):
                temp[i][M // 2 + j] = array[i][j]

        # 3 -> 2
        for i in range(N // 2, N):
            for j in range(M // 2, M):
                temp[i - N // 2][j] = array[i][j]

        # 2 -> 1
        for i in range(N // 2):
            for j in range(M // 2, M):
                temp[i][j - M // 2] = array[i][j]

        # 1 -> 4
        for i in range(N // 2):
            for j in range(M // 2):
                temp[i + N // 2][j] = array[i][j]

        array = temp

    # print("----------------------------------")
    # for row in array:
    #     print(*row)

for row in array:
    print(*row)
