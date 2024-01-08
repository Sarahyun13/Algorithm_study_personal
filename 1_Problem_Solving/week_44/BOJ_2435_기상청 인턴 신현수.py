import sys

input = sys.stdin.readline

N, K = map(int, input().split())
temps = list(map(int, input().split()))
start = 0
end = start + K
answer = []
while end <= N:
    total = sum(temps[start:end])
    answer.append(total)
    start += 1
    end += 1

print(max(answer))