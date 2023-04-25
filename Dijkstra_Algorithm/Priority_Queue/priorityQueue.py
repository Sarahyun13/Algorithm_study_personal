# 보통의 큐는 선입 선출(FIFO)의 원칙에 의하여 먼저 들어온 데이터가 먼저 나가게 된다.
# 하지만 우선순위 큐(priority queue)에서는 데이터들이 우선 순위를 가지고 있고 우선 순위가 높은 데이터가 먼저 나가게 된다.
# 힙(heap)은 완전 이진 트리의 일종으로 여러 개의 값들 중에서 가장 큰 값이나 가장 작은 값을 빠르게 찾아내도록 만들어진 자료 구조
# 최대 힙(max heap): 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리 -> 우선순위가 높은 값이 앞
# 최소 힙(min heap): 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리 -> 우선순위가 낮은 값이 앞
# 시간 복잡도는 O(log₂n)

import heapq

# 최소 힙
def minHeapSort(arr):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in arr:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내서 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


# 최대 힙 (-를 이용하여 구현)
def maxHeapSort(arr):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in arr:
        heapq.heappush(h, -value) # value에 - 붙여서 최대 힙으로

    # 힙에 삽입된 모든 원소를 차례대로 꺼내서 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h)) # - 붙였던 값에 다시 - 붙여서 원래대로 담기

    return result

result1 = minHeapSort([1,3,5,7,9,2,4,6,8,0])
print(result1)

result2 = maxHeapSort([1,3,5,7,9,2,4,6,8,0])
print(result2)