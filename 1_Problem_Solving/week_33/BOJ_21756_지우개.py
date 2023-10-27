import sys

input = sys.stdin.readline

N = int(input())
array = [i + 1 for i in range(N)]
while len(array) > 1:
    temp = []
    for i in range(len(array)):
        if i % 2 == 1:
            temp.append(array[i])

    array.clear()
    array = temp

print(*array)
