import sys

input = sys.stdin.readline

n = int(input())

# 나머지에 따라 나눠서 푼 내 풀이 -> 비효율적
# count = 0
# if n == 1 or n == 3:
#     print(-1)
# else:
#     if n % 5 == 0:
#         count = n // 5
#     elif n % 5 == 4:
#         count += n // 5
#         n = 4
#         count += n // 2
#     elif n % 5 == 3:
#         count += n // 5 - 1
#         n = 8
#         count += n // 2
#     elif n % 5 == 2:
#         count += n // 5
#         n = 2
#         count += n // 2
#     elif n % 5 == 1:
#         count += n // 5 - 1
#         n = 6
#         count += n // 2

#     print(count)

# 반복문 이용해서 풀이
count = 0
while True:
    if n % 5 == 0:
        count += n // 5
        break
    else:
        n -= 2
        count += 1

    if n < 0:
        break

if n < 0:
    print(-1)
else:
    print(count)
