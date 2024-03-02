import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().rstrip() for _ in range(N)]
count = []
# 8*8로 자르기 위해 -7을 해 준다.
for i in range(N-7):
    for j in range(M-7):
        white = 0 # 흰색으로 시작하는 경우
        black = 0 # 검은색으로 시작하는 경우

        # 시작 지점 지정
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0: # 행과 열 번호를 더했을 때 짝수인 경우,
                    if board[x][y] != 'W': # W가 아니라 B라면
                        white += 1 # 흰색으로 시작하는 경우에는 칠해야 하므로 +1
                    else: # B가 아니라 W라면
                        black += 1 # 검은색으로 시작하는 경우에는 칠해야 하므로 +1
                else: # 행과 열 번호를 더했을 때 홀수인 경우,
                    if board[x][y] != 'W': # W가 아니라 B라면
                        black += 1 # 검은색으로 시작하는 경우에는 칠해야 하므로 +1
                    else: # B가 아니라 W라면
                        white += 1 # 흰색으로 시작하는 경우에는 칠해야 하므로 +1

        count.append(white)
        count.append(black)

print(min(count))
