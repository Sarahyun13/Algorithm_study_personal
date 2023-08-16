n = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        # 인덱스 i인 현재 값이 그 전 값들보다 더 크다면
        if arr[i] > arr[j]:
            # 인덱스 i인 현재 dp값과 인덱스 j인 전 dp값 + 1 중 큰 것을 저장
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp)) # 부분 수열 길이 최댓값 출력(dp 최댓값)

count = max(dp) # 부분 수열 길이 최댓값(dp 최댓값) 저장
result = [] # 수열 저장할 리스트

for i in range(n-1, -1, -1): # dp 리스트 거꾸로 탐색
    if (dp[i] == count): # dp 값과 같다면
        result.append(arr[i]) # 주어진 수열에서 같은 인덱스 i에 있는 값을 결과 수열 리스트에 삽입
        count -= 1 # 길이 - 1

result.reverse() # 거꾸로 삽입되어 있으므로 거꾸로 정렬

# 결과 리스트 출력
for i in result:
    print(i, end = ' ')
