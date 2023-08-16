import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))

    max = 0
    profit = 0
    for i in range(N - 1, -1, -1):
        if stock[i] > max:
            max = stock[i]
        else:
            profit += max - stock[i]

    print(profit)
