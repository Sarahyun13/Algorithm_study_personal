import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    maxHeap, minHeap = [], []
    k = int(input())
    check = [False] * k # Heap에서의 존재 유무 체크

    for key in range(k):
        order, num = input().rstrip().split()
        num = int(num)
        if order == 'I':
            heapq.heappush(minHeap, (num, key))
            heapq.heappush(maxHeap, (num*-1, key))
            check[key] = True # True이면 어떤 Heap에서도 아직 삭제되지 않은 상태
        # 우선순위가 높은 노드 하나를 삭제한다.
        elif order == 'D':
            if num == -1:
                if minHeap:
                    check[minHeap[0][1]] = False # 해당 heap에서 삭제할 것이므로 False로 변경
                    heapq.heappop(minHeap) # 해당 heap에서 가장 높은 우선순위 노드 삭제
            elif num == 1:
                if maxHeap:
                    check[maxHeap[0][1]] = False
                    heapq.heappop(maxHeap)

        # check가 False라면 해당 노드가 다른 heap에서는 삭제된 상태이므로
        while minHeap and not check[minHeap[0][1]]:
            heapq.heappop(minHeap)  # 해당 heap에서도 삭제
        while maxHeap and not check[maxHeap[0][1]]:
            heapq.heappop(maxHeap)

    if minHeap and maxHeap:
        print(-maxHeap[0][0], minHeap[0][0])
    else:
        print("EMPTY")
