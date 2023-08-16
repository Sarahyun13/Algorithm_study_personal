import sys

input = sys.stdin.readline


def available(paper):
    # 주어진 문자열의 길이가 1이라면
    if len(paper) == 1:
        return True  # 가능

    # 주어진 문자열의 길이가 3 이상이라면 분할 정복 수행
    for i in range(len(paper) // 2):
        # 양 쪽 대칭으로 확인해서 수가 같다면
        if paper[i] == paper[len(paper) - 1 - i]:
            return False  # 불가능
    # 반으로 접힌 상태를 분할 정복으로 확인
    return available(paper[0 : len(paper) // 2])


#  and available(
#         paper[len(paper) // 2 + 1 : len(paper)]
#     )


T = int(input())
for _ in range(T):
    paper = list(input().rstrip())

    if available(paper):
        print("YES")
    else:
        print("NO")
