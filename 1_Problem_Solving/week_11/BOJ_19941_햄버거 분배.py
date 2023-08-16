import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = input()

visit = [0] * N
count = 0

for i in range(N):
    if arr[i] == "P":
        for j in range(i - K, i + K + 1):
            if 0 <= j < N and arr[j] == "H" and visit[j] == 0:
                visit[j] = 1
                count += 1
                break

print(count)
