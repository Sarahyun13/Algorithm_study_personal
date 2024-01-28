import sys
from collections import deque

input = sys.stdin.readline

# N: 0, S: 1
# 시계 방향: 1, 반시계 방향: -1

# 왼쪽 톱니바퀴 확인
def left(gear, direction):
    # 맨왼쪽 톱니바퀴는 확인하지 않는다
    if gear < 0:
        return

    # 다른 극이면 회전
    if gears[gear][2] != gears[gear+1][6]:
        left(gear-1, -direction)
        gears[gear].rotate(direction)



# 오른쪽 톱니바퀴 확인
def right(gear, direction):
    # 맨오르쪽 톱니바퀴는 확인하지 않는다
    if gear > 3:
        return

    # 다른 극이면 회전
    if gears[gear-1][2] != gears[gear][6]:
        right(gear+1, -direction)
        gears[gear].rotate(direction)


gears = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
K = int(input())
for _ in range(K):
    gear, direction = map(int, input().split())
    gear -= 1
    # 회전해야 할 톱니바퀴의 왼쪽, 오른쪽 톱니바퀴들의 회전 여부를 확인하고, 회전시킨다.
    # 회전해야 할 톱니바퀴 회전 방향의 반대 방향으로 회전해야 하기 때문에 -direction을 전달한다.
    left(gear-1, -direction)
    right(gear+1, -direction)
    # 회전해야 할 톱니바퀴를 회전시킨다
    gears[gear].rotate(direction)

score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += 2**i

print(score)