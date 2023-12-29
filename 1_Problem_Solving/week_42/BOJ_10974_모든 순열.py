import sys

input = sys.stdin.readline


def dfs():
    if len(seq) == N:
        print(" ".join(map(str, seq)))
        return

    for i in range(1, N + 1):
        if i in seq:
            continue
        else:
            seq.append(i)
            dfs()
            seq.pop()


N = int(input())
seq = []
dfs()
