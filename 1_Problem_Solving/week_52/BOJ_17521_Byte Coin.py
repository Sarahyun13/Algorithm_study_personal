import sys

input = sys.stdin.readline

n, W = map(int, input().split())
price = []
for _ in range(n):
    price.append(int(input().rstrip()))

coin = 0
for i in range(n):
    if i == n - 1: # 마지막 날
        # 전 날에 비해 가격이 높거나 같다면 매도
        if price[i-1] <= price[i]:
            W += coin * price[i]
            coin = 0
    elif i < n - 1: # 마지막 날이 아닌 경우
        # 다음 날 가격이 높아진다면 매수
        if price[i] < price[i+1] and (W//price[i]) > 0 :
            coin = W // price[i]
            W %= price[i]
            # print(i, coin, W)
        # 다음 날 가격이 낮아진다면 매도
        elif price[i] > price[i+1] and coin > 0:
            W += coin * price[i]
            coin = 0
            # print(i, coin, W)

print(W)