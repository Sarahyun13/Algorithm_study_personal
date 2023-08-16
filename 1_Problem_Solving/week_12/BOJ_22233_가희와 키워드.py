# 자료구조 해시를 이용
# -> 리스트가 아니라 딕셔너리로 해야 시간 초괴 문제 해결

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

memo = dict()
for _ in range(N):
    memo[input().strip()] = 1

# print(memo)
count = N
for _ in range(M):
    writing = list(input().strip().split(","))
    # print(writing)
    for keyword in writing:
        if keyword in memo.keys():
            if memo[keyword] == 1:
                memo[keyword] -= 1
                count -= 1
    print(count)
