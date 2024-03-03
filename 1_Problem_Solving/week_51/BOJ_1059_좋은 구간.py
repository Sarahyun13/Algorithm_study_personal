import sys

input = sys.stdin.readline

L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())

if n in S:
    print(0)
else:
    smallest = 1 # n이 집합 S의 가장 작은 수보다 작을 때를 대비
    largest = 0
    for i in range(L):
        if S[i] > n:
            if i > 0: # n이 집합 S의 어떤 원소보다 크다면
                smallest = S[i-1] + 1
            largest = S[i] - 1
            break
    count = 0
    for i in range(smallest, n+1):
        for j in range(n, largest+1):
            if i != j:
                count += 1
    print(count)