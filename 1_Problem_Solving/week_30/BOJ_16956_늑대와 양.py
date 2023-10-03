import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
farm = [list(input().rstrip()) for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
flag = False
for x in range(R):
    for y in range(C):
        if farm[x][y] == "W":
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C and farm[nx][ny] == "S":
                    flag = True
                    break
        elif farm[x][y] == ".":
            farm[x][y] = "D"

if flag:
    print(0)
else:
    print(1)
    for s in farm:
        print("".join(s))
