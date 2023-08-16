N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

cost, minPrice = 0, price[0]

for i in range(N-1):
    if price[i] < minPrice:
        minPrice = price[i]

    cost += road[i] * minPrice

print(cost)