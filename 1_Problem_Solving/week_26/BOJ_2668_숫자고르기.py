import sys

input = sys.stdin.readline


def dfs(first, second, num):
    first.add(num)
    second.add(nums[num])

    if nums[num] in first:
        if first == second:
            answer.update(first)
            return True
        return False
    return dfs(first, second, nums[num])


N = int(input())
nums = [0]
for i in range(1, N + 1):
    nums.append(int(input()))

answer = set()
for i in range(1, N + 1):
    first = set()
    second = set()
    if i not in answer:
        dfs(first, second, i)
