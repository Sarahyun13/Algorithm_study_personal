import sys

input = sys.stdin.readline


def dfs():
    if len(seq) == M:
        print(" ".join(map(str, seq)))
        return

    for n in nums:
        seq.append(n)
        dfs()
        seq.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
seq = []
dfs()
