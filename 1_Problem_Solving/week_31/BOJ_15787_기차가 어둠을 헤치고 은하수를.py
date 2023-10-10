import sys

input = sys.stdin.readline

N, M = map(int, input().split())
train = [[0] * 21 for _ in range(N + 1)]
for _ in range(M):
    order = list(map(int, input().split()))
    if len(order) == 3:
        if order[0] == 1:
            train[order[1]][order[2]] = 1  # 사람 승차시키기
        elif order[0] == 2:
            train[order[1]][order[2]] = 0  # 사람 하차시키기
    elif len(order) == 2:
        if order[0] == 3:
            # 한 칸씩 뒤로 가기
            for k in range(19, -1, -1):
                train[order[1]][k + 1] = train[order[1]][k]
        elif order[0] == 4:
            # 한 칸씩 앞으로 가고
            for k in range(1, 20):
                train[order[1]][k] = train[order[1]][k + 1]
            train[order[1]][20] = 0  # 마지막 20번째 자리 비우기
# print(train)
milkyWay = []  # 기차 안 승객이 앉은 상태 목록
count = 0
for i in range(1, len(train)):
    if train[i] not in milkyWay:  # 상태 목록에 존재하지 않는다면
        milkyWay.append(train[i])  # 추가하고
        count += 1  # 은하수 건넘

# print(milkyWay)
print(count)
