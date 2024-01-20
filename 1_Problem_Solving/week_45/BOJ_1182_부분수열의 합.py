import sys

input = sys.stdin.readline

def dfs(idx):
    global count

    if total and sum(total) == S:
        count += 1

    for i in range(idx, N):
        total.append(nums[i])
        dfs(i+1)
        total.pop()

N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0
total = []
dfs(0)
print(count)
