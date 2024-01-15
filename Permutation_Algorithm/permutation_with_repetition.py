# Permuation with repetion Algorithm (중복 순열 알고리즘)
# 서로 다른 n개의 원소 중에서 중복을 허락해 r개의 원소를 선택하여 일렬로 나열하는 것
# 이때 원소의 순서가 다르면 서로 다른 순열로 간주한다.
# Python itertools의 모듈을 이용하면 간단히 구현할 수 있다.
# itertools를 이용하지 않고 DFS를 이용해 직접 구현할 수 있다.

# 1부터 3까지의 숫자로 이루어진 원소를 가지고 중복 순열을 구하는 경우
from itertools import product
n = 3
r = 2
items = [1, 2, 3]

# 1. itertools를 이용하여 구현하는 방법
# 하나씩 출력하기
def permutations_with_repetition_itertools(items, r):
    product1 = product(items, repeat = r)
    for pro in product1:
        print(pro)

    # 리스트로 묶어서 한 번에 출력하기
    product2 = list(product(items, repeat = r))
    print(product2)


# 2. DFS로 구현하는 방법 (재귀가 포함되어 있음)
def permutations_with_repetition_dfs(items, r):
    def dfs(result):
        # 원하는 길이의 중복 순열이 완성되면 결과 리스트에 추가
        if len(result) == r:
            results.append(result[:])
            return

        # 모든 원소에 대해 중복을 허용하며 순열 생성
        # 순서에 따라 달라지므로 모든 원소에 대해 중복을 허용하면서 재귀를 진행
        for elem in items:
            result.append(elem)
            dfs(result)
            result.pop()

    results = []
    dfs([])
    return results
