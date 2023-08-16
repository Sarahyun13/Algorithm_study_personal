import sys

input = sys.stdin.readline

# 거꾸로 T에서 S로 문자를 하나씩 삭제하는 방법으로 풀이

S = list(input().rstrip())
T = list(input().rstrip())

while len(T) != len(S):
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T = T[::-1]

if T == S:
    print(1)
else:
    print(0)
