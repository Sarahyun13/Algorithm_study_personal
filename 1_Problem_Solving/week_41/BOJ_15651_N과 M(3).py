import sys

input = sys.stdin.readline


def dfs():
    if len(seq) == M:
        print(" ".join(map(str, seq)))
        return

    for i in range(1, N + 1):
        seq.append(i)
        dfs()
        seq.pop()


N, M = map(int, input().split())
seq = []
dfs()
