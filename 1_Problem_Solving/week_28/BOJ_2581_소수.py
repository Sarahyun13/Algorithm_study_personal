import sys

input = sys.stdin.readline

M = int(input())
N = int(input())

prime = []
for n in range(M, N + 1):
    flag = True
    if n < 2:
        flag = False
    elif n == 2:
        prime.append(n)
    elif n > 2:
        for i in range(2, n):
            if n % i == 0:
                flag = False
                break
        if flag:
            prime.append(n)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
