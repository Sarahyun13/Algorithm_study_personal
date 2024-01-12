import sys

input = sys.stdin.readline

def dfs(idx):
    if len(seven) == 7 and sum(seven) == 100:
        for n in seven:
            print(n)
        exit()

    for i in range(idx, 9):
        seven.append(dwarfs[i])
        dfs(i+1)
        seven.pop()

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input().rstrip()))
dwarfs.sort()
# print(dwarfs)
seven = []
dfs(0)
