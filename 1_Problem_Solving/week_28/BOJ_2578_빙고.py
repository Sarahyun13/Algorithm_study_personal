import sys

input = sys.stdin.readline

bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

moderator = []
for _ in range(5):
    temp = list(map(int, input().split()))
    for i in range(5):
        moderator.append(temp[i])

for i in range(25):
    