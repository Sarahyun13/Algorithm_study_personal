import sys

input = sys.stdin.readline

def dfs():
    if len(comb) == k:
        combStr = ''
        for c in comb:
            combStr += str(c)
        result.add(int(combStr))

    for i in range(n):
        if not visited[i]:
            comb.append(nums[i])
            visited[i] = True
            dfs()
            comb.pop()
            visited[i] = False

n = int(input())
k = int(input())
nums = []
for _ in range(n):
    nums.append(int(input().rstrip()))

comb = []
visited = [False] * n
result = set()
dfs()
print(len(result))