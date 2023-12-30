import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(arr, (x, 1))
    elif x < 0:
        heapq.heappush(arr, (-x, -1))
    elif x == 0:
        if arr:
            num, state = heapq.heappop(arr)
            num = num * state
            print(num)
        else:
            print(0)
