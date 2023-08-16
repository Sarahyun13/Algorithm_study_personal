import sys

input = sys.stdin.readline

dp = [0] * 1001
dp[1] = 1
for i in range(2, 1001):
    if i % 2 == 0:  # 너비가 짝수면
        dp[i] = (2 * dp[i - 1] + 1) % 10007
    else:  # 너비가 홀수면
        dp[i] = (2 * dp[i - 1] - 1) % 10007

n = int(input())
print(dp[n])
