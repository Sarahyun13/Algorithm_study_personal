import sys

input = sys.stdin.readline


def count_star(x, y):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    count = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == "*":
                count += 1

    return count


def display_star():
    for i in range(n):
        for j in range(n):
            if board[i][j] == "*":
                state[i][j] = "*"


n = int(input())
board = []
for _ in range(n):
    board.append(list(input().rstrip()))

state = []
for _ in range(n):
    state.append(list(input().rstrip()))

for i in range(n):
    for j in range(n):
        if state[i][j] == "x" and board[i][j] == ".":
            state[i][j] = count_star(i, j)
        elif state[i][j] == "x" and board[i][j] == "*":
            display_star()

for i in range(n):
    for j in range(n):
        print(state[i][j], end="")
    print()
