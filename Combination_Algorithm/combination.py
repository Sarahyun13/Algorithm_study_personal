# Combination Algorithm (조합 알고리즘)
# 서로 다른 n개의 원소 중에서 r개의 원소를 선택하여 순서를 고려하지 않고 나열하는 것
# 이때 원소의 순서가 다르더라도 같은 조합으로 간주한다.
# Python itertools의 모듈을 이용하면 간단히 구현할 수 있다.
# itertools를 이용하지 않고 재귀함수나 DFS를 이용해 직접 구현할 수 있다.

# 1부터 3까지의 숫자로 이루어진 원소를 가지고 조합을 구하는 경우
from itertools import combinations
n = 3
r = 2
items = [1, 2, 3]

# 1. itertools를 이용하여 구현하는 방법
def combinations_itertools(items, r):
    # 하나씩 출력하기
    combinations1 = combinations(items, r)
    for combination in combinations1:
        print(combination)

    # 리스트로 묶어서 한 번에 출력하기
    combinations2 = list(combinations(items, r))
    print(combinations2)


# 2. 재귀함수로 구현하는 방법
# combination_recursion([1,2,3], 2) = ([1], combination_recursion([2, 3], 1))
#                                       + ([2], combination_recursion([3], 1)))
def combinations_recursion(items, r):
    # 종료 조건: r이 0이면 더 이상 선택할 원소가 없으므로 빈 리스트 반환
    if r == 0:
        return [[]]
    
    # 조합을 담을 리스트 생성
    result = []

    # 원소 하나씩 선택하여 조합 생성
    for i, elem in enumerate(items):
        rest = items[i + 1:]
        for comb in combinations_recursion(rest, r-1):
            result.append([elem] + comb)

    return result


# 3. DFS로 구현하는 방법 (재귀가 포함되어 있음)
def combinations_dfs(items, r):
    # 현재까지 만들어진 조합의 원소들(curList)과 선택할 수 있는 시작 인덱스(start)
    def dfs(start, curList):
        # 원하는 길이의 조합이 완성되면 결과 리스트에 추가
        if len(curList) == r:
            result.append(curList[:])
            return
        
        # start부터 끝까지의 원소 중에서 하나를 선택하여 조합 생성
        for i in range(start, len(items)):
            dfs(i + 1, curList + [items[i]])

    result = []
    dfs(0, [])

    return result