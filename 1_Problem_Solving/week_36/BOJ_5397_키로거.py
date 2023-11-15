import sys
from collections import deque

input = sys.stdin.readline

# 1. 배열 1개로 해결
# deque 사용해야 함 -> 리스트 사용하면 시간 초과
T = int(input())
for _ in range(T):
    gangsan = input().rstrip()
    password = deque()
    cursor = 0
    for word in gangsan:
        if cursor > 0 and word == "<":
            cursor -= 1
        elif cursor < len(password) and word == ">":
            cursor += 1
        elif password and cursor > 0 and word == "-":
            del password[cursor - 1]
            cursor -= 1
        elif word.isalpha() or word.isalnum():
            password.insert(cursor, word)
            cursor += 1

    print("".join(password))

# 2. 배열 2개로 해결
T = int(input())
for _ in range(T):
    left = []
    right = []
    gangsan = input().rstrip()

    for word in gangsan:
        if word == "<":
            if left:
                right.append(left.pop())
        elif word == ">":
            if right:
                left.append(right.pop())
        elif word == "-":
            if left:
                left.pop()
        else:
            left.append(word)

    left.extend(reversed(right))
    print("".join(left))
