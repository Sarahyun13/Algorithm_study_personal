import sys

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    player = [0] * 10001
    for _ in range(N):
        rank = list(map(int, input().split()))
        for num in rank:
            player[num] += 1

    topScore = max(player)
    for i in range(10001):
        if player[i] == topScore:
            player[i] = 0

    secondRank = []
    secondScore = max(player)
    for i in range(10001):
        if player[i] == secondScore:
            secondRank.append(i)
    secondRank.sort()

    print(*secondRank)
