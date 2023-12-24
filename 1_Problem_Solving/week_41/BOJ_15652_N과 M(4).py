import sys

input = sys.stdin.readline


def dfs(start):
    if len(seq) == M:
        print(" ".join(map(str, seq)))
        return

    for i in range(start, N + 1):
        seq.append(i)
        dfs(i)
        seq.pop()


N, M = map(int, input().split())
seq = []
dfs(1)
