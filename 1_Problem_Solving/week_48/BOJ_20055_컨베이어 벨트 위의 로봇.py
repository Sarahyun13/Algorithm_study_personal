import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(list(map(int, input().split()))) # 벨트 위 칸의 내구도
robot = deque([0] * N) # 벨트 위의 로봇

stage = 1
while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt.rotate(1) # 벨트 회전
    robot.rotate(1) # 로봇 이동
    robot[N-1] = 0 # 내리는 위치(N-1)에서 로봇을 내린다.

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    for i in range(N-2, -1, -1): # 뒤에서부터 이동
        # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        if robot[i] and not robot[i+1] and belt[i+1] != 0:
            robot[i+1] = 1 # 이동시킨다.
            robot[i] = 0 # 원래 자리의 로봇을 없앤다.
            belt[i+1] -= 1 # 이동할 다음 위치의 내구도 감소시킨다.
    robot[N-1] = 0 # 내리는 위치(N-1)에서 로봇을 내린다.

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if belt[0] != 0:
        robot[0] = 1 # 로봇을 올린다.
        belt[0] -= 1 # 내구도를 감소시킨다.

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if belt.count(0) >= K:
        print(stage)
        break
    stage += 1
