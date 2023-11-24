import sys

input = sys.stdin.readline

# 각 블록에 대해서 왼쪽과 오른쪽 양 옆을 탐색해 두 방향 모두에서 현재 위치의 블록보다 더 높은 블록에 둘러쌓여 있으면 빗물이 고인다.
# 현재 위치의 블록을 둘러싼 왼쪽, 오른쪽 블록 중 더 낮은 블록의 높이까지 빗물이 고인다.

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

water = 0
for i in range(1, W - 1):  # 양 끝은 물이 고일 수 없다.
    leftMax = max(blocks[:i])  # 현재 위치보다 왼쪽의 블록들 중 제일 높은 블록
    rightMax = max(blocks[i + 1 :])  # 현재 위치보다 오른쪽의 블록들 중 제일 높은 블록

    lowerHeight = min(leftMax, rightMax)  # 둘 중 낮은 블록의 높이
    if blocks[i] < lowerHeight:  # 현재 위치의 블록이 lowerHeight보다 낮다면
        water += lowerHeight - blocks[i]  # 빗물이 고인다.

print(water)
