import sys

input = sys.stdin.readline

N = int(input())
price = [int(input()) for _ in range(N)]
price.sort(reverse=True)

pay = 0
for i in range(N):
    if (i + 1) % 3 == 1 or (i + 1) % 3 == 2:
        pay += price[i]

print(pay)
