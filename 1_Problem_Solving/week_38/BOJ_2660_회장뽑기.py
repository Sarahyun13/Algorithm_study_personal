import sys

input = sys.stdin.readline

n = int(input())
friends = [[] for _ in range(n + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break

    friends[a].append(b)
    friends[b].append(a)

    relations = []
    for i in range(n + 1):
        relations
