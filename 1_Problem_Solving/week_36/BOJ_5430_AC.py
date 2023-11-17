import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    array = deque(input().rstrip()[1:-1].split(","))

    # "[]"로 입력받아도 deque의 길이는 1이 되기 때문에
    # 길이가 0인 배열은 예외사항으로 빈 큐로 초기화 해줘야 한다.
    if n == 0:
        array = deque()

    R, flag = 0, 0
    for l in p:
        # R이 나올 때마다 뒤집으면 시간 초과 남
        # R이 나온 개수가 홀수일 때만 뒤집음
        if l == "R":
            R += 1
        elif l == "D":
            if len(array) == 0:  # 빈 배열이라면
                print("error")  # 에러 출력
                flag = 1  # 에러 확인 변수
                break
            else:
                if R % 2 == 0:  # R이 짝수 번 나왔다면
                    array.popleft()  # 첫번째 원소 버림
                else:  # R이 홀수 번 나왔다면
                    array.pop()  # 마지막 원소 버림

    if not flag:  # 에러가 나지 않았다면
        if R % 2 == 0:  # 짝수 번
            print("[" + ",".join(array) + "]")
        else:  # 홀수 번
            array.reverse()  # 뒤집어서 출력
            print("[" + ",".join(array) + "]")
