# LIS(Longest Increasing Subsequence) 알고리즘
# == 가장 긴 증가하는 부분 수열 알고리즘
# 움직이지 않는 아이들 == 가장 긴 증가하는 부분 수열
# 수열에 해당하는 아이들은 제외하고 나머지를 움직이는 것이 효율이 가장 좋다는 것

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

# 옮겨지는 아이들의 최소 수 = 전체 아이들의 수 - 가장 긴 증가하는 부분 수열의 길이(움직이지 않는 아이들)
print(n-max(dp))