# N과 M의 입력 범위가 (1<=N, M<=10^5)이므로 그냥 탐색으로 풀면 시간 초과가 뜰 것
# 각 범위 중 포함되는 범위 하나를 찾는 것이고, 각 범위가 순서대로 주어지기 때문에
# 이분탐색을 적용할 수 있는 문제
import sys

input = sys.stdin.readline


def binarySearch(rank, power):
    start, end = 0, len(rank) - 1

    while start <= end:
        mid = (start + end) // 2

        if power <= int(rank[mid][1]):
            end = mid - 1
        else:
            start = mid + 1

    return rank[end + 1][0]


N, M = map(int, input().split())
rank = []
for _ in range(N):
    rank.append(list(input().split()))

# print(rank)

for _ in range(M):
    power = int(input())
    print(binarySearch(rank, power))
