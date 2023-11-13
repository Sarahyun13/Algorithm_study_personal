import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
targets = list(map(int, input().split()))
array = deque([i for i in range(1, N + 1)])

count = 0
while targets:
    if targets[0] == array[0]:
        targets.pop(0)
        array.popleft()
    else:
        idx = array.index(targets[0])
        if idx <= len(array) - idx:
            count += idx
            array.rotate(-idx)
            # print(array)
            targets.pop(0)
            array.popleft()
        else:
            count += len(array) - idx
            array.rotate((len(array) - idx))
            # print(array)
            targets.pop(0)
            array.popleft()
print(count)
