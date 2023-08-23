import sys

input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
result = [0] * N
stack = []

for i in range(len(towers)):
    while stack:
        if stack[-1][1] < towers[i]:
            stack.pop()
        else:
            result[i] = stack[-1][0] + 1
            break
    stack.append((i, towers[i]))

# Python 리스트에 Asterisk(*) 를 사용하면 리스트 압축 해제를 할 수 있음
print(*result)
