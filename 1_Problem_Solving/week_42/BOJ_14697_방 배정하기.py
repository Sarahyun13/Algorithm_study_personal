import sys

input = sys.stdin.readline

A, B, C, N = map(int, input().split())

an = N // A
bn = N // B
cn = N // C
possible = False
for a in range(an + 1):
    for b in range(bn + 1):
        for c in range(cn + 1):
            if A * a + B * b + C * c == N:
                print(1)
                exit()
print(0)
