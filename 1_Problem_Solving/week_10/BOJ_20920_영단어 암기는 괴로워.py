import sys
input = sys.stdin.readline

# 단어 개수, 단어 길이
N, M = map(int, input().split())

words = {} # 딕셔너리
for _ in range(N):
    word = input().strip()

    if len(word) < M: # 단어의 길이가 M 미만이라면
        continue
    else: # 단어의 길이가 M 이상이라면
        if word in words: # 단어가 이미 존재한다면
            words[word] += 1 # 단어 빈도 수 1 증가
        else: # 새로운 단어라면
            words[word] = 1 # 단어 빈도 수에 1 삽입

# x[0] = 단어, x[1] = 단어 빈도 수
# 1. -x[1] = 자주 나오는 단어 앞에 배치(내림차순)
# 2. -len(x[0]) = 단어 길이 길수록 앞에 배치(내림차순)
# 3. x[0] = 단어 사전 순 정렬(오름차순)
words = sorted(words.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for word in words:
    print(word[0])