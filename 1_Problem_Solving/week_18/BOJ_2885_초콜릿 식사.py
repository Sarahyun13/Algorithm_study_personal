import sys

input = sys.stdin.readline

K = int(input())

size = 1
while K > size:
    size *= 2
print(size, end=" ")

count = 0
while K > 0:
    if K >= size:
        K -= size
    else:
        size //= 2
        count += 1
print(count)
