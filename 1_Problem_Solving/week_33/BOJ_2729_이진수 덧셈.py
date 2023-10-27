import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num1, num2 = input().split()
    # 이진수 내장 함수 이용
    # print(bin(int(num1, 2) + int(num2, 2))[2:])

    # 구현
    sumNum = list(str(int(num1) + int(num2)))

    while "2" in sumNum or "3" in sumNum:
        for i in range(len(sumNum) - 1, -1, -1):
            if sumNum[i] == "2":
                sumNum[i] = "0"
                if i - 1 >= 0:
                    sumNum[i - 1] = str(int(sumNum[i - 1]) + 1)
                if i - 1 < 0:
                    sumNum.insert(0, "1")
            elif sumNum[i] == "3":
                sumNum[i] = "1"
                if i - 1 >= 0:
                    sumNum[i - 1] = str(int(sumNum[i - 1]) + 1)
                if i - 1 < 0:
                    sumNum.insert(0, "1")

    answer = int("".join(sumNum))
    print(answer)
