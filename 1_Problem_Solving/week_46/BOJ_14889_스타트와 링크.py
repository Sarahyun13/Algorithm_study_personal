import sys

input = sys.stdin.readline

def dfs(start):
    if len(startList) == N//2:
        # print("start", startList)
        start, link = 0, 0
        linkList = []
        for num in range(1, N+1):
            if num not in startList:
                linkList.append(num)
        # print("link", linkList)
        for i in startList:
            for j in startList:
                start += S[i-1][j-1]
        for i in linkList:
            for j in linkList:
                link += S[i-1][j-1]
        resultList.append(abs(start-link))
        return

    for num in range(start, N+1):
        startList.append(num)
        dfs(num+1)
        startList.pop()

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

startList = []
resultList = []
dfs(1)
# print(resultList)
print(min(resultList))