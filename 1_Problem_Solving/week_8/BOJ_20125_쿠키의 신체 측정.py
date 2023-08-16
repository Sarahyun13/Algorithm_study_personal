import sys
input = sys.stdin.readline

n = int(input())
cookie = []
for i in range(n):
    cookie.append(list(input()))

leftArm, rightArm, waist, leftLeg, rightLeg = 0, 0, 0, 0, 0
heartx, hearty = 0, 0
found = False
for i in range(n):
    for j in range(n):
        if cookie[i][j] == '*':
            heartx, hearty = i + 1, j
            found = True
            break
    if found:
        break
print(heartx+1, hearty+1)

for i in range(hearty):
    if cookie[heartx][i] == '*':
        leftArm += 1

for i in range(hearty+1, n):
    if cookie[heartx][i] == '*':
        rightArm += 1

for i in range(heartx+1, n):
    if cookie[i][hearty] == '*':
        waist += 1

for i in range(heartx+waist+1, n):
    if cookie[i][hearty-1] == '*':
        leftLeg += 1
    
    if cookie[i][hearty+1] == '*':
        rightLeg += 1

print(leftArm, rightArm, waist, leftLeg, rightLeg)