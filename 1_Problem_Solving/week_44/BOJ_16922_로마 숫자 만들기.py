import sys

input = sys.stdin.readline

def dfs(idx):
    if len(nums) == N:
        result.add(sum(nums))
        return

    # 시작 구간을 반복하지 않도록 설정해야 중복 제거되며 시간 초과 나지 않음.
    for i in range(idx, len(romes)):
        nums.append(romes[i])
        dfs(i)
        nums.pop()

N = int(input())
romes = [1, 5, 10, 50]
nums = []
result = set()
dfs(0)
print(len(result))