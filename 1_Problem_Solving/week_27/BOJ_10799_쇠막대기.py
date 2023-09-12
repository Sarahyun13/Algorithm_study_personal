import sys

input = sys.stdin.readline

exp = input().rstrip()
stack = []
cut = 0
for i in range(len(exp)):
    if exp[i] == "(":
        stack.append(exp[i])
    else:
        if exp[i - 1] == "(":  # 레이저
            stack.pop()
            cut += len(stack)  # 현재 stack에 쌓인 '(' 개수(쇠막대기 개수)만큼 더해줌
        else:  # 쇠막대기의 끝
            stack.pop()
            cut += 1  # 레이저로 잘린 마지막 끝 부분인 1만 더해줌

print(cut)
