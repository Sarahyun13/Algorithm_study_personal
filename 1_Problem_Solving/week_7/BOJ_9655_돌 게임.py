import sys
input = sys.stdin.readline

n = int(input())
sk, cy = 0, 0
while(True):
    if n >= 3:
        if sk == cy:
            sk += 1
        else:
            cy += 1
        n -= 3
    elif n >= 0:
        if sk == cy:
            sk += 1
        else:
            cy += 1
        n -= 1

    if n == 0:
        if sk == cy: print("CY")
        else: print("SK")
        break

# 짝수 홀수로 나눠서 해도 됨