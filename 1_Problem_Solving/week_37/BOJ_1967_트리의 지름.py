import sys

input = sys.stdin.readline

# 트리의 지름은 dfs나 bfs를 2번 사용하여 O(n)의 시간복잡도로 구현이 가능하다.
# 1. 트리에서 아무 노드나 선택하여 그 노드에서 가장 먼 노드를 구하고 이 노드를 a라고 한다.
# 2. a에서 가장 먼 노드를 구한다. 이 노드를 b라고 한다.
# 3. a과 b의 거리가 트리의 지름이 된다.


def dfs(node):
    stack = [(0, node)]

    while stack:
        curDist, curNode = stack.pop()
        for nextDist, nextNode in graph[curNode]:
            if distance[nextNode] == -1:
                dist = curDist + nextDist
                distance[nextNode] = dist
                stack.append((dist, nextNode))


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((weight, child))
    graph[child].append((weight, parent))

# 1. 루트 노드인 1번 노드에서 가장 먼 노드를 찾는다.
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1)

# 2. 1번 과정에서 찾은 노드에서 가장 먼 노드를 찾는다.
node = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[node] = 0
dfs(node)

print(max(distance))
