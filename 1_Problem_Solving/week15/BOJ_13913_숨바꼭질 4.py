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

        if x == K:  # 목표 지점에 도달했다면(동생을 찾았다면)
            print(visited[x])  # 최단 시간 출력
            cur = K  # 마지막 위치부터 시작
            result = [K]  # 결과 리스트에 마지막 위치 삽입
            for _ in range(visited[x]):
                result.append(link[cur])  # 그 전 위치 삽입
                cur = link[cur]  # 인덱스를 그 전 위치로 변경
            result.reverse()  # 마지막 위치부터 거꾸로 저장된 것을 시작 위치부터 출력하기 위해 reverse

            for i in range(len(result)):
                print(result[i], end=" ")
            return

        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1  # 방문 처리하면서 시간 증가시킴
                link[nx] = x  # 다음 위치 인덱스에 현재 위치를 저장 (이동 경로)
                queue.append(nx)


N, K = map(int, input().split())
visited = [-1] * MAX  # 방문 처리 & 시간 저장 리스트
link = [-1] * MAX  # 이동 경로 저장 리스트

bfs(N)
