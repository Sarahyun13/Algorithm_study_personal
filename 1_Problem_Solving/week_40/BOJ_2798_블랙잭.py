import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

total = 0
combis = combinations(cards, 3)
for combi in combis:
    tempSum = sum(combi)
    if total < tempSum <= M:
        total = tempSum

print(total)
