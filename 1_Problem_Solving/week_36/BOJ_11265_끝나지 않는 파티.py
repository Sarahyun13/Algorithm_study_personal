import sys

input = sys.stdin.readline

N, M = map(int, input().split())
party = [list(map(int, input().split())) for _ in range(N)]
# 전체 경로 다 갱신해야 함
# 다른 경로에 의해 입력받은 파티장의 경로가 영향을 받을 수 있기 때문에
for k in range(N):
    for i in range(N):
        for j in range(N):
            if party[i][j] > party[i][k] + party[k][j]:
                party[i][j] = party[i][k] + party[k][j]

for _ in range(M):
    a, b, timeLimit = map(int, input().split())

    if party[a - 1][b - 1] <= timeLimit:
        print("Enjoy other party")
    else:
        print("Stay here")
