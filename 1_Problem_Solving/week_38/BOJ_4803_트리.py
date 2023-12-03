import sys

input = sys.stdin.readline


# 1. DFS를 활용한 풀이 방법
# 시작 노드부터 시작하여 DFS를 끝까지 돌고,
# 사이클 존재 여부를 리턴하는 함수
def findCycle(node):
    for next in graph[node]:
        # 인접 노드가 자신의 부모 노드인 경우 패스
        if parent[node] == next:
            continue

        # 인접 노드가 부모 노드가 아닌데 방문한 적이 있다면
        # 사이클을 의미한다.
        if visited[next]:
            return True

        parent[next] = node
        visited[next] = 1

        # 인접 노드를 루트 노드로 하는 서브트리에 사이클이 존재하면
        # 전체 트리에 사이클이 존재하는 것과 같다.
        if findCycle(next):
            return True

    return False


testCase = 0
while True:
    testCase += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    parent = [-1] * (n + 1)
    visited = [0] * (n + 1)
    count = 0
    # visited가 0인 모든 노드를 탐색하면서
    # 가능한 모든 연결 요소(연결 그래프)를 순회한다.
    for node in range(1, n + 1):
        if visited[node] == 0:
            parent[node] = node
            visited[node] = 1
            if not findCycle(node):
                count += 1

    if count == 0:
        print(f"Case {testCase}: No trees.")
    elif count == 1:
        print(f"Case {testCase}: There is one tree.")
    else:
        print(f"Case {testCase}: A forest of {count} trees.")


####################################################################################


# 2. Union-Find를 활용한 풀이 방법
def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


testCase = 0
while True:
    testCase += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    cycle = set()
    for _ in range(m):
        a, b = map(int, input().split())
        # 간선으로 연결된 두 정점 a, b의 부모가 같다면 사이클
        if find(a) == find(b):
            cycle.add(parent[a])
            cycle.add(parent[b])

        # 두 정점 중 하나가 사이클에 포함되는 정점이라면 나머지 정점도 사이클에 포함한다.
        if parent[a] in cycle or parent[b] in cycle:
            cycle.add(parent[a])
            cycle.add(parent[b])

        # 두 정점의 parent 값 갱신
        union(a, b)

    # find 함수로 전체 parent를 갱신한다.
    for i in range(n + 1):
        find(i)

    # parent에 담긴 노드들을 순회하며 사이클에 포함되지 않은 그래프만 count에 더해준다.
    parent = set(parent)
    count = sum([1 if i not in cycle else 0 for i in parent]) - 1
    if count == 0:
        print("Case %d: No trees." % testCase)
    elif count == 1:
        print("Case %d: There is one tree." % testCase)
    else:
        print("Case %d: A forest of %d trees." % (testCase, count))
