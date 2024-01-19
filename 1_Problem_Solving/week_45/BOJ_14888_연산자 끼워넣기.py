import sys

input = sys.stdin.readline

def dfs(count, total, plus, minus, multiply, divide):
    global minNum, maxNum

    if count == N:
        minNum = min(minNum, total)
        maxNum = max(maxNum, total)
        return

    if plus:
        dfs(count+1, total+nums[count], plus-1, minus, multiply, divide)
    if minus:
        dfs(count+1, total-nums[count], plus, minus-1, multiply, divide)
    if multiply:
        dfs(count+1, total*nums[count], plus, minus, multiply-1, divide)
    if divide:
        dfs(count+1, int(total/nums[count]), plus, minus, multiply, divide-1)

N = int(input())
nums = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
minNum = 1e9
maxNum = -1e9

dfs(1, nums[0], plus, minus, multiply, divide)
# 출력할 때 int로 변환해 줘야 소수점 밑의 자리 수들이 출력되지 않음
print(int(maxNum))
print(int(minNum))