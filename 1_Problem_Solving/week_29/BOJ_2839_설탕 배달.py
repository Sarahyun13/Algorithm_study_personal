import sys

input = sys.stdin.readline

N = int(input())

count = 0
while True:
    if N % 5 == 0:
        count += N // 5
        N = 0
        break
    else:
        N -= 3
        count += 1

    if N <= 0:
        break

if N == 0:
    print(count)
else:
    print(-1)
