import sys
from itertools import combinations

input = sys.stdin.readline


# 조합 직접 구현
def combinations_recursion(arr, count):
    if count == 0:
        return [[]]

    result = []
    for i, elem in enumerate(arr):
        rest = arr[i + 1 :]
        for comb in combinations_recursion(rest, count - 1):
            result.append([elem] + comb)

    return result


ex = input().rstrip()

stack = []
pair = []
result = set()  # 중복 발생 가능하므로 중복 제거하기 위해 집합 선언

# 괄호의 시작점과 끝점을 stack에 set으로 저장
for i in range(len(ex)):
    if ex[i] == "(":
        stack.append(i)
    elif stack and ex[i] == ")":
        pair.append((stack[-1], i))
        stack.pop()

# combinations을 통해 모든 경우의 수 확인
for count in range(1, len(pair) + 1):
    # cases = combinations(pair, count) # itertools 사용
    cases = combinations_recursion(pair, count)  # 직접 구현한 조합 함수 사용
    for case in cases:
        temp = list(ex)  # 문자열 복사

        for i in case:
            temp[i[0]] = ""
            temp[i[1]] = ""

        # 리스트 형태로 있는 문자들을 문자열로 합치기
        result.add("".join(temp))

# 오름차순 정렬
# 집합 형태로는 sort 사용 불가하므로 리스트로 변환 후 정렬
for answer in sorted(list(result)):
    print(answer)
