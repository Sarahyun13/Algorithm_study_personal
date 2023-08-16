import sys

input = sys.stdin.readline

N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# Top-Down 방식
dp = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    t = T[i]
    p = P[i]
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다.
    if i + t > N:
        dp[i] = dp[i + 1]
    else:  # 퇴사일을 넘기지 않는다면
        # i일에 상담을 하는 것과 상담을 안 하는 것 중 큰 것을 선택
        dp[i] = max(dp[i + 1], p + dp[i + t])

print(dp[0])
