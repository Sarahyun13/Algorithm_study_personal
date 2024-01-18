import sys

input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = [0] * w
time = 0
while bridge: # 마지막 트럭이 빠져 나갈 때까지 반복
    time += 1 # 시간이 흐르고,
    bridge.pop(0) # 다리 위의 첫 번째는 다리를 빠져 나감
    if trucks: # 아직 다리를 건너야 할 트럭이 남아 있다면
        # 다리 위의 트럭이 무게와 다음에 올라 갈 트럭의 무게를 합한 것이
        # 다리의 최대 하중보다 작다면
        if sum(bridge) + trucks[0] <= L:
            # 트럭이 다리 위를 건너 가기 시작한다.
            # 다리의 끝에 새로운 트럭을 추가한다.
            bridge.append(trucks.pop(0))
        else: # 다리의 최대 하중보다 크다면
            # 새로운 트럭 대신 다리의 남은 공간을 뜻하는 0을 추가한다.
            bridge.append(0)

print(time)