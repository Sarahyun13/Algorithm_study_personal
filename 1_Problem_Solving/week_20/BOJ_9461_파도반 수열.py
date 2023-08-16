import sys

input = sys.stdin.readline

dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1


def triangle(N):
    for i in range(4, N + 1):
        dp[i] = dp[i - 3] + dp[i - 2]

    return dp[N]


T = int(input())
for _ in range(T):
    N = int(input())
    print(triangle(N))
