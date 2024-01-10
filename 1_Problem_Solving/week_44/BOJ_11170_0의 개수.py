import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    count = 0
    N, M = map(int, input().split())
    for num in range(N, M+1):
        numStr = str(num)
        for s in numStr:
            if s == '0':
                count += 1
    print(count)