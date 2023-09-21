import sys

input = sys.stdin.readline

# 시간 초과 뜸
# if n == 2:
#     a, b = map(int, input().split())
#     for i in range(1, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             print(i)
# if n == 3:
#     a, b, c = map(int, input().split())
#     for i in range(1, min(a, b, c) + 1):
#         if a % i == 0 and b % i == 0 and c % i == 0:
#             print(i)


# 시간 초과를 방지하기 위해
# 유클리드 호제법 활용
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
nums = list(map(int, input().split()))

# gcd 함수로 최대공약수를 먼저 구한다.
g = gcd(nums[0], gcd(nums[1], nums[-1]))
# 최대공약수의 약수를 구하면 모든 공약수를 구할 수 있다.
# 약수는 그 수의 제곱근 이하의 수들만 나누어 떨어지는지 확인하면 된다.
answer = []
for i in range(1, int(g ** (1 / 2)) + 1):
    if g % i == 0:
        answer.append(i)
        if i != (g // i):  # 제곱근이라면 중복되지 않게
            answer.append(g // i)

# 2로 나눈 수까지만 확인하는 방법도 있음
# 하지만 제곱근 방식이 시간 효율성 최고
# for i in range(1, (g // 2) + 1):
#     if g % i == 0:
#         print(i)

answer.sort()  # 오름차순으로 정렬
for ans in answer:
    print(ans)
