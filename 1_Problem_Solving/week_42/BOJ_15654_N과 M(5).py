import sys

input = sys.stdin.readline


def dfs():
    if len(seq) == M:
        print(" ".join(map(str, seq)))
        return

    for i in range(N):
        if nums[i] in seq:
            continue
        else:
            seq.append(nums[i])
            dfs()
            seq.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
seq = []
dfs()
