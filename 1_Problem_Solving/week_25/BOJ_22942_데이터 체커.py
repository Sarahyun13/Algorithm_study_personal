import sys

input = sys.stdin.readline

# stack을 이용해 올바른 괄호로 구성된 식을 판별하는 문제와 같이 풀면 됨
N = int(input())
circles = []
for i in range(N):
    x, r = map(int, input().split())

    # 각 원의 왼쪽 끝점과 오른쪽 끝점을 각각 원의 번호와 함께 저장
    circles.append((x - r, i))
    circles.append((x + r, i))

# 각 원의 왼쪽 끝점을 기준으로 오름차순으로 정렬
circles.sort()

stack = []
for c in circles:
    if stack:
        # stack의 top인 원의 왼쪽 끝점이 자기 자신의 오른쪽 끝점을 만난다면(원의 번호로 확인)
        # 원의 왼쪽 끝과 오른쪽 끝 사이에 이르기까지 다른 원들과 겹치지 않는 것이므로 stack에서 pop
        if stack[-1][1] == c[1]:
            stack.pop()
        else:  # stack의 top과 원의 번호가 일치하지 않는다면
            stack.append(c)  # 스택에 추가
    else:  # stack이 비어있다면
        stack.append(c)

if stack:  # 겹치는 원이 존재해 stack에 원이 존재한다면
    print("NO")
else:  # 모든 원이 겹치지 않아 stack에 아무것도 남아있지 않다면
    print("YES")
