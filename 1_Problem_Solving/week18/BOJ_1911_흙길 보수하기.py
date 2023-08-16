import sys

input = sys.stdin.readline

N, L = map(int, input().split())
pools = [list(map(int, input().split())) for _ in range(N)]

# 웅덩이 시작 좌표를 기준으로 오름차순 정렬
pools.sort(key=lambda x: x[0])

cur = 0  # 웅덩이를 덮은 마지막 널빤지의 위치
count = 0  # 널빤지의 개수
for start, end in pools:
    if start > end:
        continue
    # 이전 웅덩이에서 덮은 널빤지가 해당 웅덩이를 덮고 있는 경우
    if cur > start:
        start = cur
    # 널빤지의 개수 카운트
    while start < end:
        start += L
        count += 1
    cur = start

print(count)
