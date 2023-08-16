for _ in range(1, 11):
    t = int(input())

    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))

    maxVal = 0

    for row in matrix:
        if sum(row) > maxVal:
            maxVal = sum(row)

    for c in range(100):
        colSumVal = 0
        for r in range(100):
            colSumVal += matrix[r][c]
        if colSumVal > maxVal:
            maxVal = colSumVal

    diagonal1 = 0
    for i in range(100):
        diagonal1 += matrix[i][i]
    if diagonal1 > maxVal:
        maxVal = diagonal1

    diagonal2 = 0
    for i in range(100):
        diagonal2 += matrix[i][100 - i - 1]
    if diagonal2 > maxVal:
        maxVal = diagonal2

    print("#{} {}".format(t, maxVal))
