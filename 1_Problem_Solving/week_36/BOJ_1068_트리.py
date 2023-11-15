import sys

input = sys.stdin.readline


def dfs(node):
    tree[node] = -2
    for i in range(N):  # 전체 트리 탐색
        if tree[i] == node:  # 해당 노드의 부모 노드가 지워야 할 노드라면
            dfs(i)  # 해당 노드랑 해당 노드의 자식 노드도 지움


N = int(input())
tree = list(map(int, input().split()))
delete = int(input())

dfs(delete)
count = 0
for i in range(N):
    if tree[i] != -2 and i not in tree:
        count += 1

print(count)
