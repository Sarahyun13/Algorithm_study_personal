def ascentNum(n):
    # 자릿수 n이 1일 때 경우의 수 초기화
    for i in range(10):
        dp[1][i] = 1

    # 자릿수 n이 2 이상일 때 경우의 수 계산
    for i in range(2, n+1):
        for j in range(10):
            # 맨 뒤에 오는 숫자가 1~9일 때는
            # 앞에 작거나 같은 수들이 모두 올 수 있으므로
            # dp[자릿수-1][0] 부터 dp[자릿수-1][맨 뒤에 오는 숫자] 까지 합
            # for k in range(j+1):
            #     dp[i][j] += dp[i-1][k]
            dp[i][j] = sum(dp[i-1][0:j+1])


n = int(input())

# 2차원 DP 테이블 초기화
# dp[자릿수][맨 뒤에 오는 숫자] = 경우의 수
dp = [[0] * 10 for _ in range(n+1)]

ascentNum(n)
print(sum(dp[n]) % 10007)