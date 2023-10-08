import sys

input = sys.stdin.readline

N = int(input())
time = list(map(int, input().split()))
time.sort()

sum = 0
for i in range(N):
    sum += time[i] * (N - i)

print(sum)
