import sys
import heapq

input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if queue:
            print((-1) * heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, (-1) * x)
