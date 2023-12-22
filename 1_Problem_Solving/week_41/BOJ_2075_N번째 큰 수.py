import sys
import heapq

input = sys.stdin.readline

# 모든 숫자를 리스트에 저장하고, 정렬하는 방법은 메모리 초과가 난다.
# 우선순위 큐를 활용하여 N개의 숫자만 저장하는 방식으로 문제를 해결해야 한다.
N = int(input())
heap = []

for _ in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        # 우선순위 큐 안에 들어있는 원소의 개수가 N개 미만이라면
        if len(heap) < N:
            heapq.heappush(heap, num)  # 우선순위 큐에 원소 삽입
        # 우선순위 큐 안에 들어있는 원소의 개수가 N개라면
        # heap의 크기를 N개로 유지
        else:
            # 우선순위 큐의 최솟값보다 작을 경우 무시
            # 우선순위 큐의 최솟값보다 클 경우
            if heap[0] < num:
                heapq.heappop(heap)  # 최솟값 제거
                heapq.heappush(heap, num)  # 새로운 값 삽입

print(heap[0])
