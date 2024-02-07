import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
    print(A[i])
    print()