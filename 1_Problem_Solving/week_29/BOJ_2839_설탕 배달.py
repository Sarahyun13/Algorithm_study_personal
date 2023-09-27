import sys

input = sys.stdin.readline

N = int(input())

"""
# 그리디 알고리즘
count = 0
while True:
    if N % 5 == 0:
        count += N // 5
        N = 0
        break
    else:
        N -= 3
        count += 1

    if N <= 0:
        break

if N == 0:
    print(count)
else:
    print(-1)
"""

# 다이나믹 프로그래밍
dp = [-1] * 5001
dp[3] = 1
dp[5] = 1
for i in range(6, 5001):
    if i % 5 == 0:
        dp[i] = dp[i - 5] + 1
