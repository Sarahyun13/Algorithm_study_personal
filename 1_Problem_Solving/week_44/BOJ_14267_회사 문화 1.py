import sys

input = sys.stdin.readline

def dfs(start):
    stack = []
    stack.append(start)

    while stack:
        cur = stack.pop()
        for next in empl[cur]:
            result[next] += result[cur]
            stack.append(next)

n, m = map(int, input().split())

empl = [[] for _ in range(n+1)]
superior = list(map(int, input().split()))
for i in range(1, n):
    empl[superior[i]].append(i+1)

result = [0] * (n+1)
# 칭찬을 입력받을 때마다 dfs를 돌리면 시간 초과가 난다.
# 한 사람이 받은 칭찬 수치를 다 더한 후, dfs를 돌아야 한다.
for _ in range(m):
    i, w = map(int, input().split())
    result[i] += w # 입력받은 후, 더하기
dfs(1) # dfs 돌린다.

for i in range(1, n+1):
    print(result[i], end = " ")