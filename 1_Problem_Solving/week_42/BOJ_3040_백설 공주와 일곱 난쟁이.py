import sys

input = sys.stdin.readline


def dfs(idx):
    if len(dwarfs) == 7:
        if sum(dwarfs) == 100:
            print("\n".join(map(str, dwarfs)))
        else:
            return

    for i in range(idx, 9):
        dwarfs.append(nums[i])
        dfs(i + 1)
        dwarfs.pop()


nums = list(int(input()) for _ in range(9))
dwarfs = []
dfs(0)
