import sys

input = sys.stdin.readline

fiveNums = sorted(list(map(int, input().split())))
answer = fiveNums[2]
while True:
    count = 0
    for num in fiveNums:
        if answer % num == 0:
            count += 1

    if count >= 3:
        print(answer)
        break
    answer += 1