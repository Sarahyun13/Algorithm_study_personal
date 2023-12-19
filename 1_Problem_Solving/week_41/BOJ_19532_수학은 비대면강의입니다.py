import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        cprime = a * x + b * y
        fprime = d * x + e * y
        if cprime == c and fprime == f:
            print(x, y)
            exit()
