import sys

input = sys.stdin.readline

n, d = map(int, input().split())
count = 0
for i in range(1, n+1):
    strd = str(d)
    count += str(i).count(strd)

print(count)