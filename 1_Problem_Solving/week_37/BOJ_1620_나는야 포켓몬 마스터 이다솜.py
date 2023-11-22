import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numKey = dict()
nameKey = dict()
for i in range(1, N + 1):
    name = input().rstrip()
    numKey[i] = name
    nameKey[name] = i

for _ in range(M):
    ques = input().rstrip()
    if ques.isdigit():
        print(numKey[int(ques)])
    else:
        print(nameKey[ques])
