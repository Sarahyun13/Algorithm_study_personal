import sys

input = sys.stdin.readline

sold = dict()
N = int(input())
for _ in range(N):
    title = input().rstrip()
    if title in sold:
        sold[title] += 1
    else:
        sold[title] = 1

maxVal = max(sold.values())
book = []
for key, val in sold.items():
    if val == maxVal:
        book.append(key)

book.sort()
print(book[0])
