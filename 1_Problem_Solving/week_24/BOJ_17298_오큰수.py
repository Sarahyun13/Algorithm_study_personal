import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
NGE = [-1] * N
stack = []

for i in range(N):
    while stack and (stack[-1][0] < seq[i]):
        tmp, idx = stack.pop()
        NGE[idx] = seq[i]
    stack.append((seq[i], i))

print(*NGE)
