import sys

input = sys.stdin.readline

N, K = map(int, input().split())
length = list(map(int, input().split()))
length = length + length[::-1]

for i in range(N * 2):
    K -= length[i]
    if K < 0:
        if i <= N:
            print(i + 1)
            break
        else:
            print(2 * N - i)
            break
