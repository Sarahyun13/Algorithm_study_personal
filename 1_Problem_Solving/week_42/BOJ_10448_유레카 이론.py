import sys

input = sys.stdin.readline

# 삼각수 배열
# 45번째 삼각수 == 1035이므로 45까지 저장
triNum = [i * (i + 1) // 2 for i in range(1, 46)]

# 3개의 삼각수로 만들어지는 수들을 저장
eureka = [0] * 1001
for i in triNum:
    for j in triNum:
        for k in triNum:
            num = i + j + k
            if num <= 1000:
                eureka[num] = 1

testCase = int(input())
for _ in range(testCase):
    K = int(input())
    print(eureka[K])
