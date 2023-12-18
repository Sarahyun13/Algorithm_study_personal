import sys
from itertools import permutations
from copy import deepcopy

input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
rcs = [list(map(int, input().split())) for _ in range(K)]
answer = sys.maxsize

# 순열로 회전 순서 정하기 (최대 6!=720 이므로 시간복잡도 OK)
for permu in permutations(rcs, K):
    # 회전
    copyA = deepcopy(A)  # 원본 배열 복사
    for r, c, s in permu:
        r -= 1
        c -= 1
        for k in range(s, 0, -1):
            temp = copyA[r - k][c + k]

            # 위쪽
            copyA[r - k][c - k + 1 : c + k + 1] = copyA[r - k][c - k : c + k]

            # 왼쪽
            for row in range(r - k, r + k):
                copyA[row][c - k] = copyA[row + 1][c - k]

            # 아래쪽
            copyA[r + k][c - k : c + k] = copyA[r + k][c - k + 1 : c + k + 1]

            # 오른쪽
            for row in range(r + k, r - k, -1):
                copyA[row][c + k] = copyA[row - 1][c + k]

            copyA[r - k + 1][c + k] = temp

    for row in copyA:
        answer = min(answer, sum(row))

print(answer)
