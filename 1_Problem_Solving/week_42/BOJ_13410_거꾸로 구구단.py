import sys

input = sys.stdin.readline

N, K = map(int, input().split())
mul = []

for i in range(1, K + 1):
    num = N * i
    mul.append(int(str(num)[::-1]))

print(max(mul))
