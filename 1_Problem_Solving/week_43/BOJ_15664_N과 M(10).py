import sys

input = sys.stdin.readline

def dfs(idx):
    if len(seq) == M:
        print(*seq)
        return

    prev = 0
    for i in range(idx, N):
        if not visited[i] and nums[i] != prev:
            prev = nums[i]
            visited[i] = True
            seq.append(nums[i])
            dfs(i+1)
            visited[i] = False
            seq.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
seq = []
visited = [False] * N
dfs(0)
