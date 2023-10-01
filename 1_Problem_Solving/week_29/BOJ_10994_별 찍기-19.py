import sys

input = sys.stdin.readline


# n에 따라 (4*n-3)만큼의 행과 열이 생기며
# 행 + 2, 열 + 2 만큼 더해준 내부는 그 전 n-1까지의 과정이 계속 반복됨을 알 수 있다.
# -> 재귀로 풀 수 있음
def drawStars(n, idx):
    if n == 1:
        stars[idx][idx] = "*"
        return
    l = 4 * n - 3

    for i in range(idx, idx + l):
        stars[idx][i] = "*"
        stars[idx + l - 1][i] = "*"

        stars[i][idx] = "*"
        stars[i][idx + l - 1] = "*"

    return drawStars(n - 1, idx + 2)


n = int(input())
len = 4 * n - 3
stars = [[" "] * len for _ in range(len)]

drawStars(n, 0)

for i in range(len):
    for j in range(len):
        print(stars[i][j], end="")
    print()
