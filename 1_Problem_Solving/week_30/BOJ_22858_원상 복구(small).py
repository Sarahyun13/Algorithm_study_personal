import sys

input = sys.stdin.readline

N, K = map(int, input().split())
Si = list(map(int, input().split()))
D = list(map(int, input().split()))

for _ in range(K):
    temp = [0] * len(Si)
    for i in range(len(D)):
        temp[D[i] - 1] = Si[i]
    Si = temp

print(*Si)
