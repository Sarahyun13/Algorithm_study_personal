import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()  # 센서들의 위치 오름차순 정렬

# 인접한 센서들 간의 거리 차이
dist = []
for i in range(N - 1):
    dist.append(sensor[i + 1] - sensor[i])
dist.sort()  # 거리도 오름차순 정렬

# K개의 구간으로 센서들이 나뉘어야 집중국의 수신 가능 영역의 길이 합이 최소가 된다.
# 따라서 거리들의 차를 오름차순 정렬한 리스트에서 N-K개를 앞에서부터 더해준다.
# 앞에서부터 N-K개를 더해준다는 것은 센서 간의 거리의 차가 가장 큰 값을 K-1개 빼주는 것과 같다.
print(sum(dist[: N - K]))
