from collections import deque
import sys

input = sys.stdin.readline
MAX = 100001


def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 0

    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            return

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and visited[nx] == -1:
                if nx == x * 2:  # 순간이동일 경우
                    visited[nx] = visited[x]  # 0초
                    # 순간이동이므로 높은 우선순위 부여하기 위해 큐의 앞에 값 추가
                    queue.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1  # 1초
                    queue.append(nx)


N, K = map(int, input().split())
visited = [-1] * MAX

bfs(N)
