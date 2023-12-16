import sys

input = sys.stdin.readline

N = int(input())
find = False
for num in range(1, N):
    total = num
    answer = num
    while num > 0:
        total += num % 10
        num //= 10

    if total == N:
        find = True
        break

if find:
    print(answer)
else:
    print(0)
