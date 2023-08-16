str1 = ' ' + input() # 첫 열을 0으로 초기화하기 위해 열 하나 추가
str2 = ' ' + input() # 첫 행을 0으로 초기화하기 위해 행 하나 추가
len1 = len(str1)
len2 = len(str2)


# 풀이1: 2차원 배열 이용
# 첫 번째 문자열의 길이만큼 열 개수, 두 번째 문자열의 길이만큼 행 개수 설정
# 공통 수열 길이 값을 나타내는 2차원 DP 테이블
dp = [[0] * len2 for _ in range(len1)]

for i in range(1, len1):
    for j in range(1, len2):
        if str1[i] == str2[j]: # 같은 문자일 경우
            dp[i][j] = dp[i-1][j-1] + 1 # 이전 값에서 1을 더하여 저장
        else: # 다른 문자일 경우
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 기존에 있던 왼쪽 값과 위쪽 값 중 큰 값을 대입

print(dp[-1][-1])


# 풀이2: 1차원 배열 이용
# 첫 번째 문자열의 길이만큼 길이 설정
dp2 = [0] * len1

# 같은 문자를 마주하는 경우 누적 값에서 1 더한 값을 넣어주는 방식
for i in range(1, len2):
    count = 0 # 누적값 초기화
    for j in range(1, len1):
        if count < dp2[j]:
            count = dp2[j] # 누적값 변수에 이전 위치까지의 최댓값 저장
        elif str1[j] == str2[i]: # 같은 문자일 경우
            dp2[j] = count + 1 # 누적값 변수에 1 더해서 현재 위치에 저장

print(max(dp2))