import sys
input = sys.stdin.readline

N, X = map(int, input().split())
guest = list(map(int, input().split()))

if max(guest) == 0:
    print("SAD")
else:
    value = sum(guest[0:X]) # 처음 값은 0부터 X-1까지의 합

    maxVal = value
    maxCount = 1

    # 슬라이딩 윈도우
    # 크기가 고정적인 창문(특정 범위)을 옆으로 밀면서 이동하는 방식
    # 중복된 항목은 이전의 결과를 최대한 활용
    for i in range(X, N):
        value += guest[i]
        value -= guest[i-X]

        if value > maxVal:
            maxVal = value
            maxCount = 1
        elif value == maxVal:
            maxCount += 1

    print(maxVal)
    print(maxCount)