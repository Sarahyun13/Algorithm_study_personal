import sys

input = sys.stdin.readline

def dfs(idx):
    if len(seq) == M:
        print(*seq)
        return

    prev = 0
    for i in range(idx, N):
        if prev != nums[i]:
            seq.append(nums[i])
            dfs(i)
            seq.pop()
            prev = nums[i]

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
seq = []
dfs(0)
