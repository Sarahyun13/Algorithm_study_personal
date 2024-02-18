import sys

input = sys.stdin.readline

while True:
    try:
        N, M = map(int, input().split())
    except:
        break

    count = 0
    for num in range(N, M+1):
        flag = True
        numStr = str(num)
        for i in range(10):
            iStr = str(i)
            if numStr.count(iStr) > 1:
                flag = False
        if flag:
            count += 1
    print(count)