import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    inst = input().rstrip()

    if inst == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif inst == "size":
        print(len(queue))
    elif inst == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif inst == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif inst == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif inst[:4] == "push":
        num = int(inst[5:])
        queue.append(num)
