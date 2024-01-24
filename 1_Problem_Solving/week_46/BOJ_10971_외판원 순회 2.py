import sys

input = sys.stdin.readline

def dfs(cost):
    if len(path) == N:
        tempCost = W[path[-1]-1][N-1]
        if tempCost: # 길이 있는지 확인하는 것이 중요!
            costs.append(cost + tempCost)
        return

    for city in range(1, N+1):
        tempCost = W[path[-1]-1][city-1]
        # 아직 가보지 않았고, 길이 있다면
        if city not in path and tempCost:
            path.append(city)
            dfs(cost + tempCost)
            path.pop()

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
path = [N]
costs = []
dfs(0)
print(min(costs))