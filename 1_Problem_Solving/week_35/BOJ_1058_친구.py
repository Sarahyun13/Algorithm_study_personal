# A와 B가 2-친구
# -> A - B or A - C - B
# 가장 유명한 사람: 2-친구 수가 가장 많은 사람
import sys

input = sys.stdin.readline

N = int(input())
relationship = [list(input().rstrip()) for _ in range(N)]

friends = 0
for a in range(N):
    count = 0
    C = []
    for b in range(N):
        if relationship[a][b] == "Y":
            C.append(b)
            count += 1

    for b in range(N):
        if a == b:
            continue
        if relationship[a][b] == "N":
            for c in C:
                if relationship[c][b] == "Y":
                    count += 1
                    break

    friends = max(friends, count)

print(friends)

"""
friends = [[0] * N for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if relationship[i][j] == "Y" or (relationship[i][k] == "Y" and relationship[k][j] == "Y"):
                friends[i][j] = 1

friendCount = 0
for row in friends:
    friendCount = max(friendCount, sum(row))
print(friendCount)
"""
