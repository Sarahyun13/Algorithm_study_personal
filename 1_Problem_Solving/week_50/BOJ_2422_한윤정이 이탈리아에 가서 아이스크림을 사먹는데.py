import sys

input = sys.stdin.readline

N, M = map(int, input().split())
worst = []
for _ in range(M):
    worst.append(list(map(int, input().split())))

# print(worst)
comb = set()
for i in range(M):
    temp = worst[i]
    # print(temp)
    for n in range(1, N+1):
        if n not in temp and len(temp)<3:
            temp.append(n)
            comb.add(tuple(sorted(temp)))
            temp.pop()
# print(comb)
result = (N*(N-1)*(N-2)) // 6 - len(comb)
print(result)