import sys
import math

input = sys.stdin.readline

n = int(input())


# DP
# n보다 작거나 같은 제곱수를 찾고, n-제곱수를 인덱스로 가진 값에 1을 더해준다.
dp = [0, 1]  # 제곱수 합의 최소 개수를 저장하는 dp 배열
for i in range(2, n + 1):
    minVal = 4
    for j in range(1, int(math.sqrt(i)) + 1):
        minVal = min(minVal, dp[i - j**2])

    dp.append(minVal + 1)

print(dp[n])


"""
# Brute Force
bf = [0 if i**0.5 % 1 else 1 for i in range(n + 1)]  # 제곱수는 1로 저장
minVal = 4
for i in range(int(n**0.5), 0, -1):
    if bf[n]:  # n이 제곱수이면
        minVal = 1
        break
    elif bf[n - i**2]:  # n이 제곱수가 아니고, n-(n보다 작은 제곱수)가 제곱수라면
        minVal = 2
        break
    else:  # n에서 n보다 작은 제곱수를 2번 뺀 수가 제곱수일 경우
        for j in range(int((n - i**2) ** 0.5), 0, -1):
            if bf[(n - i**2) - j**2]:
                minVal = 3

print(minVal)
"""
