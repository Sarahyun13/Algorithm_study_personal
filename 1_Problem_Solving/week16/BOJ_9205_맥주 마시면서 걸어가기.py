from collections import deque
import sys

input = sys.stdin.readline


def bfs(homex, homey):
    queue = deque()
    queue.append((homex, homey))

    while queue:
        x, y = queue.popleft()

        # 현재 좌표에서 페스티벌까지 갈 수 있다면
        if abs(x - festx) + abs(y - festy) <= 1000:
            print("happy")
            return
        for i in range(n):  # 편의점 리스트 확인
            if visited[i] == 0:  # 방문하지 않은 편의점이라면
                nx, ny = store[i]  # 편의점의 좌표를 다음 좌표로 설정
                if abs(x - nx) + abs(y - ny) <= 1000:  # 다음 좌표까지 갈 수 있다면
                    visited[i] = 1  # 방문 처리
                    queue.append((nx, ny))  # 다음 장소 큐에 저장

    print("sad")
    return


t = int(input())  # 테스트 케이스
for _ in range(t):
    n = int(input())  # 편의점 개수
    homex, homey = map(int, input().split())  # 집 위치

    store = []  # 편의점 위치 담을 리스트
    for _ in range(n):
        x, y = map(int, input().split())
        store.append((x, y))  # 편의점 위치 저장

    festx, festy = map(int, input().split())  # 페스티벌 위치

    visited = [0 for _ in range(n + 1)]  # 편의점 방문 처리용 리스트
    bfs(homex, homey)
