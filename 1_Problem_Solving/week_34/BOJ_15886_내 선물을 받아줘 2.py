# E:(1, x+1), W:(1, x-1)
import sys

input = sys.stdin.readline

N = int(input())
mapStr = input().rstrip()
count = 0
# 어느 곳에서 시작하든 항상 EW가 있는 곳에서 머무르게 된다.
# 즉, EW의 개수를 세어주면 된다.
for i in range(N - 1):
    if mapStr[i : i + 2] == "EW":
        count += 1
print(count)
