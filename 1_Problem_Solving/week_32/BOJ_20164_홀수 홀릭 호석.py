import sys

input = sys.stdin.readline


def solve(n: str, count: int):
    global minCnt, maxCnt

    if len(n) == 1:
        minCnt = min(minCnt, count + countOdd(n))
        maxCnt = max(maxCnt, count + countOdd(n))
        return
    elif len(n) == 2:
        solve(str(int(n[0]) + int(n[1])), count + countOdd(n))
    elif len(n) >= 3:
        for i in range(1, len(n) - 1):
            for j in range(i + 1, len(n)):
                solve(str(int(n[:i]) + int(n[i:j]) + int(n[j:])), count + countOdd(n))


def countOdd(n: str):
    oddCnt = 0
    for i in n:
        if int(i) % 2 == 1:
            oddCnt += 1
    return oddCnt


N = input().rstrip()
minCnt, maxCnt = 1e9, 0
solve(N, 0)
print(minCnt, maxCnt)
