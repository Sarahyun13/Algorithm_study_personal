import sys

input = sys.stdin.readline


def solv(arr, start):
    if not arr:
        return
    minChar = min(arr)
    minIdx = arr.index(minChar)
    result[start + minIdx] = minChar
    print("".join(result))
    solv(arr[minIdx + 1 :], start + minIdx + 1)
    solv(arr[:minIdx], start)


inputStr = input().rstrip()
result = [""] * len(inputStr)
solv(inputStr, 0)
