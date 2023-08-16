import sys

input = sys.stdin.readline

mustPay = int(input())
change = 1000 - mustPay

coins = [500, 100, 50, 10, 5, 1]
count = 0
for coin in coins:
    count += change // coin
    change %= coin

print(count)
