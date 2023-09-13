import sys
from collections import deque

input = sys.stdin.readline

"""
# 시간 초과 남
octal = input().rstrip()
# 8진수 -> 10진수
eight = 1
decimal = 0
for _ in range(len(octal)):
    octal = list(octal)
    decimal += eight * int(octal.pop())
    eight *= 8

# print(decimal)

# 10진수 -> 2진수
binary = deque()
while decimal:
    binary.appendleft(decimal % 2)
    decimal //= 2

for num in binary:
    print(num, end="")
"""

# 파이썬 내장 함수 bin() 사용
octal = int(input().rstrip(), 8)  # 입력을 8진수로 변환
print(
    bin(octal)[2:]
)  # 변환된 이후에 맨 앞 2자리에 이진법을 의미하는 0b가 붙기 때문에 2번째 자리부터 출력될 수 있도록 [2:]를 붙인다.
