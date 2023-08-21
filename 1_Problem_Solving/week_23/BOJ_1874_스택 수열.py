import sys

input = sys.stdin.readline

n = int(input())
stack = []
answer = []
cur = 1
flag = 0
for _ in range(n):
    num = int(input())
    # 입력한 수가 나올 때까지 오름차순으로 push
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1

    # stack의 top이 입력한 수와 같다면
    if stack[-1] == num:
        stack.pop()  # stack의 top을 꺼내 수열을 만든다.
        answer.append("-")
    # stack의 top이 입력한 수가 아니라면 주어진 스택을 만들 수 없다.
    else:
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)
else:
    print("NO")
