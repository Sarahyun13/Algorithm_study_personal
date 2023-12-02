import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothesDict = dict()
    for _ in range(n):
        clothes = list(input().rstrip().split())
        if clothes[1] in clothesDict:
            clothesDict[clothes[1]] += 1
        else:
            clothesDict[clothes[1]] = 1

    count = 1
    # 옷 종류마다 개수+1(하나의 종류에서 아무것도 선택하지 않았을 경우인 1 추가)
    # 경우의 수 곱하기
    for key in clothesDict:
        count *= clothesDict[key] + 1

    # 모든 옷 종류에서 아무것도 선택하지 않아
    # 아무것도 입지 않는 경우인 1 빼고 출력
    print(count - 1)
