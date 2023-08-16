import sys

input = sys.stdin.readline

N = int(input())
guess = [int(input().rstrip()) for _ in range(N)]

guess.sort()
# print(guess)
sum = 0
for i in range(N):
    sum += abs((i + 1) - guess[i])

print(sum)
