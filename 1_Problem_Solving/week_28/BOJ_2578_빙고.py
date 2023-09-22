import sys

input = sys.stdin.readline

bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))


# 사회자가 부르는 수를 일렬로 리스트에 저장
moderator = []
for _ in range(5):
    moderator += list(map(int, input().split()))
    # temp = list(map(int, input().split()))

    # for i in range(5):
    #     moderator.append(temp[i])

# 하나씩 수를 지워감
for i in range(25):
    count = 0
    for r in range(5):
        for c in range(5):
            if moderator[i] == bingo[r][c]:
                bingo[r][c] = 0
    # 수를 하나 지울 때마다 빙고인지 확인
    # 가로 줄(행) 확인
    for r in range(5):
        # print("행")
        # print(bingo[r])
        if sum(bingo[r]) == 0:
            count += 1

    # 세로 줄(열) 확인
    for c in range(5):
        # print("열")
        # print(*bingo)
        # print(list(zip(*bingo))[c])
        if sum(list(zip(*bingo))[c]) == 0:
            count += 1

    # 대각선 확인
    diagonalSum1 = 0
    diagonalSum2 = 0
    for k in range(5):
        diagonalSum1 += bingo[k][k]
        diagonalSum2 += bingo[k][4 - k]
    if diagonalSum1 == 0:
        count += 1
    if diagonalSum2 == 0:
        count += 1

    # for l in bingo:
    #     print(l)
    # print(count)

    if count >= 3:
        print(i + 1)
        break
