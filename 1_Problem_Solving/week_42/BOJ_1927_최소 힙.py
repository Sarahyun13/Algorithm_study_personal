import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    elif x > 0:
        heapq.heappush(arr, x)
