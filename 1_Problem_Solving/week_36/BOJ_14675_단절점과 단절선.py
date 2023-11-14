import sys

input = sys.stdin.readline

N = int(input())
vertex = [[] for _ in range(N + 1)]
bridge = [[] for _ in range(N)]
for i in range(1, N):
    a, b = map(int, input().split())
    vertex[a].append(b)
    vertex[b].append(a)
    if a not in bridge[i]:
        bridge[i].append(a)
    if b not in bridge[i]:
        bridge[i].append(b)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if len(vertex[k]) >= 2:
            print("yes")
        else:
            print("no")
    elif t == 2:
        if len(bridge[k]) >= 2:
            print("yes")
        else:
            print("no")
