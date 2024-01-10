import sys
from math import ceil

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    midVal = []
    M = int(input())
    seq = []
    for _ in range(ceil(M/10)):
        seq += list(map(int, input().split()))
    for i in range(0, len(seq), 2):
        temp = seq[:i+1]
        temp.sort()
        midVal.append(temp[(i+1)//2])

    print(len(midVal))
    for i in range(len(midVal)):
        if i > 0 and i % 10 == 0:
            print()
        print(midVal[i], end=" ")
