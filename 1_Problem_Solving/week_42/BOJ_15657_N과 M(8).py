import sys

input = sys.stdin.readline


def dfs(idx):
    if len(seq) == M:
        print(" ".join(map(str, seq)))
        return

    for i in range(idx, N):
        seq.append(nums[i])
        dfs(i)
        seq.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
seq = []
dfs(0)
