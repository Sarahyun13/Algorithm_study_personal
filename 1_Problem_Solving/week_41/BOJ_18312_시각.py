import sys

input = sys.stdin.readline

# 3초 => 03초로 나타냄을 유의
N, K = map(int, input().split())

count = 0
for hour in range(0, N + 1):
    for minute in range(0, 60):
        for second in range(0, 60):
            secStr = str(second)
            minStr = str(minute)
            houStr = str(hour)
            if len(secStr) == 1:
                secStr = "0" + secStr
            if len(minStr) == 1:
                minStr = "0" + minStr
            if len(houStr) == 1:
                houStr = "0" + houStr
            k = str(K)
            if k in secStr or k in minStr or k in houStr:
                count += 1
                # print(secStr, minStr, houStr)

print(count)
