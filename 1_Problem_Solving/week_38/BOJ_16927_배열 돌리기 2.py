import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]


# 1. 배열 그대로 회전시키는 방법
# pypy3로 제출 -> python3로 제출하면 시간 초과 남.
# 깊이: 몇 번이나 안쪽으로 들어가야 하는지
# 회전시켜야 하는 테두리 수
depth = min(N, M) // 2

# 깊이만큼 안으로 계속 들어간다.
for k in range(depth):
    # 한 테두리에 있는 수의 개수
    # 정확히 수의 개수만큼 회전시키면 원위치로 돌아온다.
    # 즉, 수의 개수 == 원상복구 되는 회전 수
    # 4x4 행렬일 경우 첫번째 테두리에 있는 수의 개수는 12개
    # 그러므로 12바퀴를 돌리면 원상복구 된다.
    # 식은 (2 * (한 행에 있는 수의 개수 + 한 열에 있는 수의 개수)) - 2번씩 중복된 네 모서리
    comeBack = (2 * ((N - 2 * k) + (M - 2 * k))) - 4

    # 전체 회전 수에서 원상복구 되는 회전 수로 나머지 연산 수행하여
    # 수의 위치 변화에 영향을 미치는 회전 수만큼만 회전시킨다.
    for _ in range(R % comeBack):
        temp = array[k][k]  # 첫번째 수 저장시켜 놓기

        # 위쪽 행 이동 시키기
        for i in range(1 + k, M - k):
            array[k][i - 1] = array[k][i]

        # 오른쪽 열 이동 시키기
        for i in range(1 + k, N - k):
            array[i - 1][M - 1 - k] = array[i][M - 1 - k]

        # 아래쪽 행 이동 시키기
        for i in range(1 + k, M - k):
            array[N - 1 - k][M - i] = array[N - 1 - k][M - 1 - i]

        # 왼쪽 열 이동 시키기
        for i in range(1 + k, N - k):
            array[N - i][k] = array[N - 1 - i][k]

        # 저장했던 첫번째 수가 이동할 위치로
        array[1 + k][k] = temp

for row in array:
    print(*row)


# 2. deque에 테두리 넣어서 회전시키는 방법
# python3로 제출해도 시간 초과 나지 않음
depth = min(N, M) // 2
for k in range(depth):
    queue = deque()
    # queue.extend(array[k][k:M-k])
    # queue.extend([row[M-k-1] for row in array[k+1:N-k-1]])
    # queue.extend(array[N-k-1][k:M-k][::-1])
    # queue.extend([row[k] for row in array[k+1:N-k-1]][::-1])

    # 위쪽 행 큐에 삽입
    for j in range(k, M - k):
        queue.append(array[k][j])
    # 오른쪽 열 큐에 삽입
    for j in range(k + 1, N - k - 1):
        queue.append(array[j][M - k - 1])
    # 아래쪽 행 큐에 삽입
    for j in range(M - k - 1, k - 1, -1):
        queue.append(array[N - k - 1][j])
    # 왼쪽 열 큐에 삽입
    for j in range(N - k - 2, k, -1):
        queue.append(array[j][k])

    queue.rotate(-R)  # 회전 수만큼 회전시키기

    # 위쪽 행 배열에 삽입
    for j in range(k, M - k):
        array[k][j] = queue.popleft()
    # 오른쪽 열 배열에 삽입
    for j in range(k + 1, N - k - 1):
        array[j][M - k - 1] = queue.popleft()
    # 아래쪽 행 배열에 삽입
    for j in range(M - k - 1, k - 1, -1):
        array[N - k - 1][j] = queue.popleft()
    # 왼쪽 열 배열에 삽입
    for j in range(N - k - 2, k, -1):
        array[j][k] = queue.popleft()

for row in array:
    print(*row)
