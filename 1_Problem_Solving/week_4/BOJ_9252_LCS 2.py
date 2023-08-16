str1 = ' ' + input()
str2 = ' ' + input()
len1 = len(str1)
len2 = len(str2)

dp = [[0] * len2 for _ in range(len1)]

# 풀이1
# LCS로 길이 구한 뒤, dp 배열의 뒤에서부터 역추적하여 문자열 출력
for i in range(1, len1):
    for j in range(1, len2):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

x = len1 - 1 # 첫 번째 문자열의 길이
y = len2 - 1 # 두 번째 문자열의 길이
result = "" # 결과 문자열 저장할 변수
# 배열의 뒤인 맨 오른쪽 아래에서부터 시작하여 현재 값과 일치하는 숫자 방향으로 인덱스 이동시킨다
while x > 0 and y > 0: # 맨 위로 갈 때까지
    if dp[x][y] == dp[x][y-1]: # 현재 값이 왼쪽 값과 같다면
        y-=1 # 왼쪽으로 이동
    elif dp[x][y] == dp[x-1][y]: # 현재 값이 위쪽 값과 같다면
        x-=1 # 위쪽으로 이동
    else: # 위나 왼쪽에 같은 수가 없다면
        result = str1[x] + result # 현재 인덱스에 맞는 문자를 결과 문자열에 더한 후
        x-=1; y-=1 # 대각선 왼쪽 위로 이동

if result:
    print(result)


# 풀이2
# dp 배열을 문자열 자체로 두고, 길이 값과 결과 문자열 값 한 번에 저장
dp2 = [[""] * len2 for _ in range(len1)]

for i in range(1, len1):
    for j in range(1, len2):
        if str1[i] == str2[j]: # 같은 문자일 경우
            dp2[i][j] = dp2[i-1][j-1] + str1[i] # 이전 값에서 현재 인덱스에 맞는 문자 더해서 저장
        else: # 다른 문자일 경우
            # 기존에 있던 왼쪽 값과 위쪽 값의 길이 중
            if len(dp2[i-1][j]) >= len(dp2[i][j-1]): # 위쪽 값의 길이가 더 크거나 같다면
                dp2[i][j] = dp2[i-1][j] # 위쪽 값 저장
            else: # 왼쪽 값의 길이가 더 크다면
                dp2[i][j] = dp2[i][j-1] # 왼쪽 값 저장

result2 = dp2[-1][-1]
print(len(result), result, sep="\n")