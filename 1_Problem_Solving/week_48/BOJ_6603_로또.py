import sys

input = sys.stdin.readline

def dfs(idx):
    if len(result) == 6:
        print(*result)
        return

    for i in range(idx, len(S)):
        result.append(S[i])
        dfs(i+1)
        result.pop()

while True:
    S = list(map(int, input().split()))
    k = S.pop(0)

    if k == 0:
        break
    result = []
    dfs(0)
    print()