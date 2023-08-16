import sys

input = sys.stdin.readline

fib = [[0] * 2 for _ in range(41)]
fib[0][0] = 1
fib[1][1] = 1
for i in range(2, 41):
    fib[i][0] = fib[i - 1][0] + fib[i - 2][0]
    fib[i][1] = fib[i - 1][1] + fib[i - 2][1]

T = int(input())
for _ in range(T):
    N = int(input())
    print("{0} {1}".format(fib[N][0], fib[N][1]))
