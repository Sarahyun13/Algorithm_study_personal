# Dynamic Programming (동적 계획법)
# 동일한 작은 문제들이 반복적으로 계산되는 경우
# 동일한 문제를 매번 재계산 하지 않고 값을 저장했다가 재사용하는 기법
# 처음 계산하는 연산은 기록, 이미 계산했던 연산이라면 기록되어 있는 값 호출
# 메모리 공간을 약간 더 사용하여 시간을 획기적으로 줄일 수 있는 방법
# Top-Down(Memoization)_하향식 방식: 큰 문제를 해결하기 위해 작은 문제를 호출한다
#                                   -> 한 번 구한 계산 결과를 메모리 공간에 기록해두고, 같은 식을 다시 호출하면 기록한 결과 그대로 가져오는 기법
# Bottom-Up(Tabulation)_상향식 방식: 하위 문제부터 시작해서 더 큰 문제를 해결해 나간다 (작은 문제부터 큰 문제까지 하나하나 테이블을 채워간다)
#                                   -> 하위 문제부터 천천히 해결하면서 더 큰 문제를 해결하는 기법
# 대표적인 동적계획법 문제 - 피보나치 수열


# 1. Top-Down 방식

# 한 번 계산된 결과를 memoization 하기 위한 리스트
memo = [0] * 100

# 피보나치 수열을 재귀함수로 구현
def fiboMemo(n):
    if n == 1 or n == 2:
        return 1
    
    if memo[n] != 0:
        return memo[n]
    
    memo[n] = fiboMemo(n-1) + fiboMemo(n-2)
    return memo[n]



# 2. Bottom-Up 방식

# 작은 문제부터 해결해서 저장할 dp 테이블
dp = [0] * 100

# 피보나치 수열을 반복문으로 구현
def fiboTab(n):
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]