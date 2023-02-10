# Divide & Conquer(분할정복)
# 어떤 문제를 더 이상 쪼갤 수 없을 때까지 분할한 후 (Divide)
# 분할한 작은 문제들을 해결하고 (Conquer)
# 합치면서 (Combine) 문제의 답을 도출하는 알고리즘
# 대표적인 분할정복 문제 - 병합정렬(Merge Sort), 퀵정렬(Quick Sort)


# 1. 병합정렬 (Merge Sort)
# 정렬할 리스트를 더 이상 나눌 수 없을 때까지 최소 단위로 분할 (Divide)
# 다시 합치면서 정렬 수행 (Conquer, Combine)
# 시간복잡도: O(nlogn)
def mergeSort(arr):
    if len(arr) < 2:
        return arr  # 사이즈가 2보다 작을 경우 바로 리턴
    
    # Divide - 크기가 1이 될 때까지 재귀 호출
    mid = len(arr) // 2
    leftArr = mergeSort(arr[:mid])
    rightArr = mergeSort(arr[mid:])

    resultArr = [] # 분할된 리스트를 병합하여 결과 리스트 생성
    l = r = 0 # 분할 리스트의 인덱스
    while l < len(leftArr) and r < len(rightArr): # 왼쪽과 오른쪽 리스트 중 하나의 끝에 도달할 때까지
        if leftArr[l] < rightArr[r]: # 왼쪽 값이 오른쪽 값보다 작을 때
            resultArr.append(leftArr[l]) # 결과 리스트에 왼쪽 값 삽입
            l += 1 # 왼쪽만 인덱스 증가
        else: # 오른쪽 값이 왼쪽 값보다 작을 때
            resultArr.append(rightArr[l]) # 결과 리스트에 오른쪽 값 삽입
            r += 1 # 오른쪽만 인덱스 증가
    
    # 끝에 도달하지 않은 리스트의 나머지 값들을 결과 리스트에 삽입
    resultArr += leftArr[l:]
    resultArr += rightArr[r:]

    return resultArr



# 2. 퀵정렬 (Quick Sort)
# 리스트에서 임의의 값을 기준 값 pivot으로 정함
# pivot을 기준으로 pivot보다 작은 값들은 왼쪽에 큰 값들은 오른쪽에 위치시킴
# pivot을 제외한 왼쪽, 오른쪽 리스트에 대해 반복 (Divide)
# 다시 합침 (Conquer, Combine)
def quickSort1(arr):
    if len(arr) < 2: 
        return arr # 사이즈가 2보다 작을 경우 바로 리턴
    
    pivot = arr[len(arr) // 2] # 리스트의 가운데 값을 pivot으로 선택
    leftArr, equalArr, rightArr = [], [], []
    for num in arr:
        if num < pivot:
            leftArr.append(num) # pivot보다 작다면 왼쪽에 위치시킴
        elif num > pivot:
            rightArr.append(num) # pivot보다 크다면 오른쪽에 위치시킴
        else:
            equalArr.append(num) # pivot이랑 같다면 다른 리스트에 저장
    
    return quickSort1(leftArr) + equalArr + quickSort1(rightArr)


def quickSort2(arr):
    def sort(left, right):
        if left <= right:
            return
        
        mid = partition(left, right)
        sort(left, mid - 1)
        sort(mid, right)

    def partition(left, right):
        pivot = arr[(left + right) // 2] # 리스트의 가운데 값을 pivot으로 선택
        while left <= right: # 왼쪽 인덱스가 오른쪽 인덱스보다 커질 때까지, 즉 교차될 때까지
            while arr[left] < pivot: # 왼쪽 인덱스가 가리키는 값이 pivot보다 작은 경우
                left += 1 # 인덱스 값 증가시킴 -> pivot보다 큰데 왼쪽에 있는 값을 찾기 위해
            while arr[right] > pivot: # 오른쪽 인덱스가 가리키는 값이 pivot보다 큰 경우
                right -= 1 # 인덱스 값 증가시킴 -> pivot보다 작은데 오른쪽에 있는 값을 찾기 위해
            if left <= right: # 왼쪽 인덱스가 오른쪽 인덱스보다 작거나 같다면, 즉 교차되지 않았다면
                arr[left], arr[right] = arr[right], arr[left] # 잘못된 위치에 있는 두 값의 위치 변경
                left, right = left + 1, right - 1 # 인덱스도 이동시킴
        
        return left # 다음 재귀 호출의 분할 기준점이 될 인덱스 리턴
    
    return sort(0, len(arr) - 1)
