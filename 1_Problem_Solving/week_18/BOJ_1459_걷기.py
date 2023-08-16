import sys

input = sys.stdin.readline

x, y, w, s = map(int, input().split())
minVal = min(x, y)
absVal = abs(x - y)

if 2 * w <= s:
    print((x + y) * w)
elif w < s:
    print(minVal * s + absVal * w)
elif s <= w:
    if absVal % 2 == 0:
        print(minVal * s + absVal * s)
    else:
        print(minVal * s + (absVal - 1) * s + w)
