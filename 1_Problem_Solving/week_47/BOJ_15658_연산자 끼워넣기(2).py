import sys

input = sys.stdin.readline

def dfs(result, idx, plus, minus, multiply, divide):
    global maxNum, minNum

    if idx == N:
        maxNum = max(maxNum, result)
        minNum = min(minNum, result)

    if idx < N:
        if plus:
            dfs(result + nums[idx], idx+1, plus-1, minus, multiply, divide)
        if minus:
            dfs(result - nums[idx], idx+1, plus, minus-1, multiply, divide)
        if multiply:
            dfs(result * nums[idx], idx+1, plus, minus, multiply-1, divide)
        if divide:
            dfs(int(result / nums[idx]), idx+1, plus, minus, multiply, divide-1)


N = int(input())
nums = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
maxNum, minNum = -1e9, 1e9
dfs(nums[0], 1, plus, minus, multiply, divide)
print(maxNum)
print(minNum)