import sys

input = sys.stdin.readline

N = int(input())
draw = [[input().rstrip() for _ in range(5)] for _ in range(N)]
compare = []
for a in range(N-1):
    for b in range(a+1, N):
        count = 0
        for i in range(5):
            for j in range(7):
                if draw[a][i][j] != draw[b][i][j]:
                    count += 1
        compare.append((count, a+1, b+1))

result = min(compare)
print(result[1], result[2])