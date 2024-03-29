def stairsNum(n):
    # 자릿수 n이 1일 때 경우의 수 초기화
    for i in range(1, 10):
        dp[1][i] = 1

    # 자릿수 n이 2 이상일 때 경우의 수 계산
    for i in range(2, n+1):
        for j in range(10):
            if j == 0: # 맨 뒤에 오는 숫자가 0일 때는
                # 앞에 1만 올 수 있으므로 경우의 수 1
                # dp[자릿수-1][맨 뒤 숫자+1]
                dp[i][j] = dp[i-1][j+1]
            elif 0 < j < 9: # 맨 뒤에 오는 숫자가 1~8일 때는
                # 앞에 1씩 크거나 작은 수가 올 수 있으므로 경우의 수 2
                # dp[자릿수-1][맨 뒤 숫자-1] + dp[자릿수-1][맨 뒤 숫자+1]
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            elif j == 9: # 맨 뒤에 오는 숫자가 9일 때는
                # 앞에 8만 올 수 있으므로 경우의 수 1
                # dp[자릿수-1][맨 뒤 숫자-1]
                dp[i][j] = dp[i-1][j-1]


n = int(input())

# 2차원 DP 테이블 초기화
# dp[자릿수][맨 뒤에 오는 숫자] = 경우의 수
dp = [[0] * 10 for _ in range(n+1)]

stairsNum(n)

print(sum(dp[n]) % 1000000000)