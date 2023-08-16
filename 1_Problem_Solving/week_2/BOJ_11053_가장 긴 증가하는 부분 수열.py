def partialSequence(n):
    for i in range(n):
        for j in range(i):
            # 인덱스 i의 값이 그 전 값들보다 더 크고, 현재까지의 최댓값보다 크다면
            if arr[i] > arr[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1 # DP 테이블 최댓값 + 1로 업데이트

n = int(input())
arr = list(map(int, input().split()))

# DP 테이블 0으로 초기화
dp = [1 for i in range(n)]

partialSequence(n)
print(max(dp))