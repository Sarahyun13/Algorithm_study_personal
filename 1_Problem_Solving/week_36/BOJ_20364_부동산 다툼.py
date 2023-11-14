import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
area = [0] * (N + 1)
for i in range(1, Q + 1):
    order = []
    areaNum = int(input())
    # 원하는 땅까지 가는 길에 거쳐가는 땅 리스트에 담기
    while areaNum >= 1:
        order.append(areaNum)
        areaNum = areaNum // 2
    # print(order)

    while order:
        now = order.pop()
        if not order and not area[now]:  # 원하는 땅에 도착했고, 가질 수 있다면
            area[now] = i  # 땅 리스트에 주인 오리 번호 대입
            print(0)  # 가짐 출력
        elif area[now] != 0:  # 원하는 땅까지 가는 길에 다른 오리가 이미 점유한 땅이 존재한다면
            print(now)  # 점유한 땅 출력
            break
    # print(area)
