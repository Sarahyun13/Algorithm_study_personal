import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, d = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    # print(array)

    count = abs(d) // 45
    result = [[0] * n for _ in range(n)]
    temp = [[0] * n for _ in range(n)]
    # 배열 복사
    for i in range(n):
        for j in range(n):
            temp[i][j] = array[i][j]
            result[i][j] = array[i][j]

    for k in range(count):
        if d > 0:  # 시계 방향
            for i in range(n):
                result[i][n // 2] = temp[i][i]
                result[i][n - 1 - i] = temp[i][n // 2]
                result[n // 2][i] = temp[n - 1 - i][i]
                result[i][i] = temp[n // 2][i]

        if d < 0:  # 반시계 방향
            for i in range(n):
                result[i][i] = temp[i][n // 2]
                result[i][n // 2] = temp[i][n - 1 - i]
                result[i][n - 1 - i] = temp[n // 2][n - 1 - i]
                result[n // 2][i] = temp[i][i]

        # 배열 복사
        for i in range(n):
            for j in range(n):
                temp[i][j] = result[i][j]

    # print(array)
    # print(result)
    for row in result:
        print(*row)
