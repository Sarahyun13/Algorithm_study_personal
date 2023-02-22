# Binary Search (이진 탐색)
# 오름차순으로 정렬된 배열을 반으로 나누어 탐색하여 원하는 수를 찾는 알고리즘
# 시간복잡도: O(log N) -> 탐색할 배열의 크기가 계속해서 반씩 줄어들기 때문에

# 배열의 중간 값 data[mid]와 찾고자 하는 값 target과 비교
# data[mid]가 target보다 크다면 data[mid]의 왼쪽 부분을 대상으로,
# data[mid]가 target보다 작다면 data[mid]의 오른쪽 부분을 대상으로 탐색
# 찾고자 하는 수의 위치에 따라 start와 end의 위치 변경

# 1. 반복문 사용
def binarySearch1(target, data):
    start = 0
    end = len(data) - 1

    while(start <= end):
        mid = (start + end) // 2 # 시작 인덱스와 마지막 인덱스 사이의 중간 인덱스

        if(data[mid] == target): # 중간 값과 target이 같다면
            return mid # 중간 인덱스 리턴 후 탐색 종료
        elif(data[mid] < target): # 중간 값이 target보다 작다면
            # 중간 값 기준 오른쪽 구간으로 이동
            # 시작 인덱스를 중간 인덱스 + 1로 변경
            start = mid + 1
        else: # 중간 값이 target보다 크다면
            # 중간 값 기준 왼쪽 구간으로 이동
            # 마지막 인덱스를 중간 인덱스 - 1로 변경
            end = mid - 1
    
    return None # 찾는 값이 없다면 None 리턴
        


# 2. 재귀 사용
def binarySearch2(target, data, start, end):
    if start > end: # 찾는 값이 없다면
        return None # None 리턴
    
    mid = (start + end) // 2 # 시작 인덱스와 마지막 인덱스 사이의 중간 인덱스
    
    if (data[mid] == target): # 중간 값과 target이 같다면
        return mid # 중간 인덱스 리턴 후 탐색 종료
    elif(data[mid] < target): # 중간 값이 target보다 작다면
        # 중간 값 기준 오른쪽 구간으로 이동
        # 시작 인덱스를 중간 인덱스 + 1로 변경
        return binarySearch2(target, data, mid+1, end)
    else: # 중간 값이 target보다 크다면
        # 중간 값 기준 왼쪽 구간으로 이동
        # 마지막 인덱스를 중간 인덱스 - 1로 변경
        return binarySearch2(target, data, start, mid-1)