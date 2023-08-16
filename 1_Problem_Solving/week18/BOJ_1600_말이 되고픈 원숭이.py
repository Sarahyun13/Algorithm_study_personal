from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    queue = deque()
    queue.append((0, 0, 0))

    while queue:
        x, y, z = queue.popleft()
        if x == H - 1 and y == W - 1:
            return visited[x][y][z]

        # 특수 이동(말처럼)을 늘린다고 하여 그때의 도착 결과가 최소 동작 횟수를 보장하지는 않는다.
        # 따라서 일반적인 동서남북 4방향으로 탐색한 후, 큐에 넣어주고
        # 현재 특수 이동을 한 횟수가 K보다 작다면 특수 이동의 방향으로 탐색해 본다.
        # 특수 이동 횟수를 고려해야 하므로 3차원 리스트를 이용한다.
        for i in range(4):
            nx = x + monkeyDx[i]
            ny = y + monkeyDy[i]

            if (
                0 <= nx < H
                and 0 <= ny < W
                and not visited[nx][ny][z]
                and not graph[nx][ny]
            ):
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
        if z < K:
            for i in range(8):
                nx = x + horseDx[i]
                ny = y + horseDy[i]

                if (
                    0 <= nx < H
                    and 0 <= ny < W
                    and not visited[nx][ny][z + 1]
                    and not graph[nx][ny]
                ):
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1
                    queue.append((nx, ny, z + 1))

    return -1


K = int(input())
W, H = map(int, input().split())
graph = []
for _ in range(H):
    graph.append(list(map(int, input().split())))

monkeyDx = [-1, 1, 0, 0]
monkeyDy = [0, 0, -1, 1]
horseDx = [-2, -1, 1, 2, 2, 1, -1, -2]
horseDy = [-1, -2, -2, -1, 1, 2, 2, 1]

print(bfs())
