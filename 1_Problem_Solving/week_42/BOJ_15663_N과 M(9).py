import sys

input = sys.stdin.readline

def dfs():
    if len(seq) == M:
        print(*seq)
        return

    prev = 0 # 그 전 숫자가 같은지 확인 -> 중복된 수열 생성하는지 확인
    for i in range(N):
        # 수가 중복되지 않고, 방문한 적 없다면
        if nums[i] != prev and not visited[i]:
            prev = nums[i]
            seq.append(nums[i])
            visited[i] = True
            dfs()
            seq.pop()
            visited[i] = False

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * N # 방문했는지 확인
seq = []
dfs()