import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0] * (N + 1)
    for _ in range(N - 1):
        p, c = map(int, input().split())
        parent[c] = p
    a, b = map(int, input().split())
    # a와 b가 부모-자식 관계일 수 있으니 인덱스 에러가 나지 않도록 0을 처음에 삽입
    a_parents = [0, a]
    b_parents = [0, b]
    while parent[a]:
        a_parents.append(parent[a])
        a = parent[a]
    while parent[b]:
        b_parents.append(parent[b])
        b = parent[b]

    # 뒤에서부터 거꾸로 탐색하며 가장 가까운 공통 조상을 찾는다.
    # 루트 노드부터 탐색하면서 서로 부모가 달라지는 지점 바로 직전이 가장 가까운 공통 조상이 된다.
    i = 1
    while a_parents[-i] == b_parents[-i]:
        i += 1

    print(a_parents[-i + 1])
