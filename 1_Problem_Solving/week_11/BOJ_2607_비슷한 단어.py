import sys

input = sys.stdin.readline

n = int(input())
first = list(input())  # 비교 대상 단어(첫 단어)
answer = 0

for _ in range(n - 1):
    compare = first[:]  # 첫 단어 복사해서 리스트에 저장
    word = input()  # 비교할 단어(새로운 단어)
    count = 0  # 비교해서 첫 단어에 없는 문자가 새로운 단어에 있다면 증가시킬 변수

    for w in word:  # 새로운 단어의 문자 하나씩
        if w in compare:  # 첫 단어에 존재한다면
            compare.remove(w)  # 첫 단어 리스트에서 삭제
        else:  # 존재하지 않는다면
            count += 1  # count 변수 1 증가

    # 첫 단어에 존재하지 않는 문자의 개수와 남아있는 문자의 개수가 모두 2보다 작다면
    if count < 2 and len(compare) < 2:
        answer += 1  # 비슷한 단어 1 증가

print(answer)
