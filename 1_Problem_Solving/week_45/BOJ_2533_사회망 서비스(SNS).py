import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

# 트리 구조와 DP를 합친 Tree DP 문제
# 트리에서 현재 노드는 얼리어답터가 되거나 되지 않을 수 있다.
# dp[현재 노드][얼리어답터 여부]
# 부모가 얼리어답터가 아닌 경우: 자식들은 모두 얼리어답터여야 한다.
#   => dp[parent][0] += dp[child][1]
# 부모가 얼리어답터인 경우: 자식들은 얼리어답터여도 되고, 아니어도 된다.
#   => dp[parent][1] += min(dp[child])

def dfs(node):
    for next in graph[node]:
        if not visited[next]:
            visited[next] = True
            dfs(next)
            dp[node][0] += dp[next][1] # 얼리어답터가 아닌 경우
            dp[node][1] += min(dp[next]) # 얼리어답터인 경우

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 1] for _ in range(N+1)]
visited = [False] * (N+1)
visited[1] = True
dfs(1)
print(min(dp[1]))
