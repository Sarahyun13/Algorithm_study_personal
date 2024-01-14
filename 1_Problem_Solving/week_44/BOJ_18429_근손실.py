import sys

input = sys.stdin.readline

def dfs(weight):
    global count

    if len(order) == N:
        count += 1
        return

    for i in range(N):
        if i in order or weight+kit[i]-K < 0:
            continue
        else:
            order.append(i)
            dfs(weight+kit[i]-K)
            order.pop()

N, K = map(int, input().split())
kit = list(map(int, input().split()))
order = []
count = 0
dfs(0)
print(count)
