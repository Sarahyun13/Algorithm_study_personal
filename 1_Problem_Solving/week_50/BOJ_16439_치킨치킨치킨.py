import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
prefer = [list(map(int, input().split())) for _ in range(N)]

result = []
chicken = list(i for i in range(M))
for comb in combinations(chicken, 3):
    total = 0
    for student in prefer:
        total += max(student[comb[0]], student[comb[1]], student[comb[2]])
    result.append(total)

print(max(result))