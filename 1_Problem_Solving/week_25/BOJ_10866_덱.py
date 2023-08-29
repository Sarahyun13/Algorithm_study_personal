import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
deq = deque()
for _ in range(N):
    inst = input().split()

    if inst[0] == "push_front":
        deq.appendleft(inst[1])
    elif inst[0] == "push_back":
        deq.append(inst[1])
    elif inst[0] == "pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif inst[0] == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif inst[0] == "size":
        print(len(deq))
    elif inst[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif inst[0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif inst[0] == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)
