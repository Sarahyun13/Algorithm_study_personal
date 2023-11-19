import sys

input = sys.stdin.readline

# 연산자 우선 순위
# 1. ()
# 2. *, /
# 3. +, -

infix = list(input())
stack = []
answer = ""

for s in infix:
    if s.isalpha():
        answer += s
    else:
        if s == "(":
            stack.append(s)  # stack에 넣어준다.
        elif s == ")":
            # '('가 나올 때까지 stack에 쌓인 연산자들 pop하고 결과 문자열에 붙여준다.
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()  # 마지막으로 스택에서 '(' pop한다.
        elif s == "*" or s == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(s)
        elif s == "+" or s == "-":  # '+', '-'가 우선순위가 제일 낮으니까
            # 괄호 안이나 괄호 밖 등 같은 우선순위에 있는 식의 연산자들 모두 pop하고 결과 문자열에 붙여준다.
            while stack and (stack[-1] != "("):
                answer += stack.pop()
            stack.append(s)

# stack에 남아 있는 원소들 모두 다 pop하고 결과 값에 붙여준다.
while stack:
    answer += stack.pop()

print(answer)
