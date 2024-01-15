# Combination with repetition Algorithm (중복 조합 알고리즘)
# 서로 다른 n개의 원소 중에서 중복을 허락해 r개의 원소를 선택하여 순서를 고려하지 않고 나열하는 것
# 이때 원소의 순서가 다르더라도 같은 조합으로 간주한다.
# Python itertools의 모듈을 이용하면 간단히 구현할 수 있다.
# itertools를 이용하지 않고 DFS를 이용해 직접 구현할 수 있다.

# 1부터 3까지의 숫자로 이루어진 원소를 가지고 조합을 구하는 경우
from itertools import combinations_with_replacement
n = 3
r = 2
items = [1, 2, 3]


# 1. itertools를 이용하여 구현하는 방법
def combinations_itertools(items, r):
    # 하나씩 출력하기
    combinations1 = combinations_with_replacement(items, r)
    for combination in combinations1:
        print(combination)

    # 리스트로 묶어서 한 번에 출력하기
    combinations2 = list(combinations_with_replacement(items, r))
    print(combinations2)


# 2. DFS로 구현하는 방법 (재귀가 포함되어 있음)
def combinations_with_repetion_dfs(items, r):
    def dfs(start, result):
        # 원하는 길이의 중복 조합이 완성되면 결과 리스트에 추가
        if len(result) == r:
            results.append(result[:])
            return

        # 중복을 허용하며 조합 생성
        # 순서가 상관없으니 시작 인덱스부터 끝까지의 원소에 대해 중복을 허용하면서 재귀를 진행
        for i in range(start, len(items)):
            result.append(items[i])
            dfs(i, result)
            result.pop()

    results = []
    dfs(0, [])
    return results
