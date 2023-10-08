# 태그: <알파벳 소문자 or 공백>
# 단어: 알파벳 소문자 or 숫자
# 태그 != 단어
# 단어만 뒤집어서 출력
import sys

input = sys.stdin.readline

S = input().rstrip()
tag = False
stack = ""
result = ""
for s in S:
    if tag:  # 태그라면
        result += s  # 결과 문자열에 바로 이어붙임
        if s == ">":  # 태그의 끝
            tag = False  # 태그 끝 표시
    else:  # 태그가 아니라면(태그 바깥 글자들이라면)
        if s == "<":  # 태그의 시작
            result += stack[::-1]  # 단어의 끝이므로 태그 전에 스택에 집어넣은 글자들 다 뒤집어서 결과 문자열에 이어붙임
            result += s  # 태그의 시작도 결과 문자열에 이어붙임
            stack = ""  # 스택 비움
            tag = True  # 태그 시작 표시
        elif s == " ":  # 태그 바깥에서 공백을 만나면
            result += (
                stack[::-1] + " "
            )  # 단어의 끝이므로 공백 전에 스택에 집어넣은 글자들 다 뒤집어서 결과 문자열에 이어붙임
            stack = ""  # 스택 비움
        else:  # 태그 바깥에서의 문자라면
            stack += s  # 단어이기 때문에 스택에 삽입

# 마지막으로 스택에 남아있는 단어 뒤집어서 이어붙임
result = result + stack[::-1]
print(result)
