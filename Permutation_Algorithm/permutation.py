# Permuation Algorithm (순열 알고리즘)
# 서로 다른 n개의 원소 중에서 r개의 원소를 선택하여 일렬로 나열하는 것
# 이때 원소의 순서가 다르면 서로 다른 순열로 간주한다.
# Python itertools의 모듈을 이용하면 간단히 구현할 수 있다.
# itertools를 이용하지 않고 재귀함수나 DFS를 이용해 직접 구현할 수 있다.

# 1. itertools를 이용하여 구현하는 방법
# 1부터 3까지의 숫자로 이루어진 원소를 가지고 순열을 구하는 경우
from itertools import permutations
n = 3
r = 2
items = [1, 2, 3]

# 하나씩 출력하기
permutations1 = permutations(items, r)
for permutation in permutations1:
    print(permutation)

# 리스트로 묶어서 한 번에 출력하기
permutations2 = list(permutations(items, r))
print(permutations2)


# 2. 재귀함수로 구현하는 방법
# permutation([1,2,3], 2) = ([1], permutation([2, 3], 1))
#                             + ([2], permutation([1, 3], 1))
#                             + ([3], permutation([1, 2], 1))
def permutations_recursion(arr, r):
    # 종료 조건: r이 0이면 더 이상 선택할 원소가 없으므로 빈 리스트 반환
    if r == 0:
        return [[]]
    
    # 순열을 담을 리스트 생성
    result = []

    # 원소 하나씩 선택하여 순열 생성
    for i, elem in enumerate(arr):
        rest = arr[:i] + arr[i+1:]
        for perm in permutations_recursion(rest, r-1):
            result.append([elem] + perm)

    return result


# 3. DFS로 구현하는 방법 (재귀가 포함되어 있음)
def permutations_dfs(arr, r):
    def dfs(curList):
        # 원하는 길이의 순열이 완성되면 결과 리스트에 추가
        if len(curList) == r:
            result.append(curList[:])
            return
        
        # 아직 선택하지 않은 원소 중에서 하나를 선택하여 순열 생성
        for i in range(len(arr)):
            if not visited[i]: # 아직 방문하지 않았다면
                visited[i] = True # 방문 처리하고
                curList.append(arr[i]) # 현재까지의 리스트에 값 추가

                dfs(curList)

                # 방금 전 리스트에 추가한 값과 방문 처리 한 것을 되돌려주기
                visited[i] = False
                curList.pop()

    result = []
    visited = [False] * len(arr)
    dfs([])

    return result