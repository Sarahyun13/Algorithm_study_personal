import sys

input = sys.stdin.readline

N = int(input())
building = []
for _ in range(N):
    building.append(int(input()))

stack = []
result = 0
# 모든 빌딩 탐색
for i in range(N):
    # stack에 값이 존재하고, 현재 빌딩의 높이가 stack의 top보다 크거나 같을 때까지
    while stack and building[i] >= stack[-1]:
        # 현재 빌딩의 높이가 top보다 작아질 때까지 stack의 top 제거
        stack.pop()

    # 현재 빌딩을 stack에 삽입
    stack.append(building[i])

    # stack에 존재하는 빌딩 수에서 자기 자신 뺀 수 결과에 더함
    result += len(stack) - 1

print(result)
