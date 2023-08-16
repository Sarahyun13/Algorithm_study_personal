import sys
input = sys.stdin.readline

n, newScore, p = map(int, input().split())
if n == 0:
    print(1)
else:
    rankList = list(map(int, input().split()))
    if len(rankList) == p and newScore <= rankList[p-1]:
        print(-1)
    else:
        rank = n + 1 # 새로운 값이 제일 작을 때
        for i in range(n):
            if newScore >= rankList[i]:
                rank = i + 1
                break
        print(rank)