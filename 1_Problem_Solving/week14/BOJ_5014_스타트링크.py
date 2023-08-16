from collections import deque
import sys

input = sys.stdin.readline


def bfs(cur):
    queue = deque()
    queue.append(cur)
    visited[cur] = 1

    while queue:
        cur = queue.popleft()
        if cur == G:
            return visited[cur] - 1
        else:
            for nex in (cur + U, cur - D):
                if 0 < nex <= F and visited[nex] == 0:
                    visited[nex] = visited[cur] + 1
                    queue.append(nex)

    return "use the stairs"


# F: 전체 층, S: 현 위치, G: 목적지, U: 위로, D: 아래로
F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)

print(bfs(S))
