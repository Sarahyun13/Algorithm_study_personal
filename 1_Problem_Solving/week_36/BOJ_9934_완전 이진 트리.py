import sys

input = sys.stdin.readline


def makeTree(cities, level):
    mid = len(cities) // 2
    tree[level].append(cities[mid])

    if len(cities) == 1:
        return
    makeTree(cities[:mid], level + 1)
    makeTree(cities[mid + 1 :], level + 1)


K = int(input())
cities = list(map(int, input().split()))
tree = [[] for _ in range(K)]

makeTree(cities, 0)
for row in tree:
    print(*row)
