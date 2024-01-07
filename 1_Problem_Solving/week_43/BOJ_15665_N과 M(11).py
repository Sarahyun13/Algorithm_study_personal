import sys

input = sys.stdin.readline

def dfs():
    if len(seq) == M:
        print(*seq)
        return

    prev = 0
    for i in range(N):
        if prev != nums[i]:
            seq.append(nums[i])
            prev = nums[i]
            dfs()
            seq.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
seq = []
dfs()

# nums 입력받을 때 set으로 변환 시켰다가 다시 list로 변환시켜서 중복 방지도 가능