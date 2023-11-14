import sys

input = sys.stdin.readline


# 루트 노드에서 모든 노드까지의 거리를 visited 배열에 저장한다.
def dfs(node):
    stack = []
    stack.append(node)

    while stack:
        now = stack.pop()
        for next in tree[now]:
            if not visited[next]:
                stack.append(next)
                visited[next] = visited[now] + 1


N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (N + 1)
dfs(1)

count = 0
for i in range(1, N + 1):
    if len(tree[i]) == 1:  # 리프 노드라면
        count += visited[i]  # 거리 다 더함

# 말을 각자 가지고 있는 것이 아니라, 같은 말을 사용해서 자기 차례에 부모 노드로 이동시킴
# 말의 이동 가능 횟수가 짝수라면 형석이 차례에서 모든 말이 사라지게 되므로 성원이가 지게 될 것이고,
# 홀수라면 성원이 차례에서 모든 말이 사라지게 되므로 성원이가 이긴다.
# 그러므로, 성원이가 게임을 이기기 위해서는 말의 총 이동 가능 횟수가 홀수여야 한다.
if count % 2 == 0:  # 말의 이동 가능 횟수가 짝수라면
    print("No")  # 진다
else:  # 말의 이동 가능 횟수가 홀수라면
    print("Yes")  # 이긴다
