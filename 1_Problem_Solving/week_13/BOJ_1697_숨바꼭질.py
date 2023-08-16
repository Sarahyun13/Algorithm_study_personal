from collections import deque
import sys

input = sys.stdin.readline


def bfs(n):
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()

        if x == K:
            print(numAry[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and not numAry[nx]:
                numAry[nx] = numAry[x] + 1
                queue.append(nx)


N, K = map(int, input().split())
MAX = 100001
numAry = [0] * MAX

bfs(N)
