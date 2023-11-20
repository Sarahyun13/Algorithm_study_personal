import sys

input = sys.stdin.readline


# C++에는 algorithm 헤더에 next_permutation이라는 함수가 있다.
# 주어진 단어의 알파벳들로 만들 수 있는 단어들을 사전 순으로 정렬했을 때,
# 주어진 단어의 다음에 오는 단어를 찾는 알고리즘
# 순열
def nextPermutation(word):
    # 1. 끝에서부터 비교해 앞 원소가 더 작은 곳의 인덱스를 i로 정한다.
    i = len(word) - 2
    while i >= 0 and word[i] >= word[i + 1]:
        i -= 1
    # 맨 끝의 원소보다 더 작은 원소가 앞에 존재하지 않는다면
    # 주어진 단어가 마지막 순서의 단어이므로
    # 그냥 주어진 단어를 출력하기 위해 False 리턴
    if i == -1:
        return False

    # 2. 끝에서부터 인덱스 i의 값보다 큰 값의 인덱스를 j로 정한다.
    j = len(word) - 1
    while word[i] >= word[j]:
        j -= 1

    # 3. 인덱스 i의 값과 인덱스 j의 값을 바꾼다.
    word[i], word[j] = word[j], word[i]
    # 4. 인덱스 i까지는 그대로 넣어 준다.
    answer = word[: i + 1]
    # 5. 인덱스 i+1부터 마지막까지는 순서를 뒤집어 넣어 준다.
    answer.extend(list(reversed(word[i + 1 :])))
    return answer


T = int(input())
for _ in range(T):
    word = list(input().rstrip())
    answer = nextPermutation(word)
    if not answer:  # 주어진 단어가 마지막 단어
        print("".join(word))  # 그대로 출력
    else:  # 다음에 나타나는 단어 출력
        print("".join(answer))
