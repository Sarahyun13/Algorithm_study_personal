import sys

input = sys.stdin.readline

H, Y = map(int, input().split())

# 투자 방식을 매년 바꿀 수 있음에 주의
dp = [0] * (Y+1)
dp[0] = H
for year in range(1, Y+1):
    if year >= 5:
        dp[year] = int(max(dp[year-1] * 1.05, dp[year-3] * 1.2, dp[year-5] * 1.35))
    elif year >= 3:
        dp[year] = int(max(dp[year-1] * 1.05, dp[year-3] * 1.2))
    else:
        dp[year] = int(dp[year - 1] * 1.05)

print(dp[Y])