import sys

input = sys.stdin.readline

left, right = input().split()
string = input().rstrip()

keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
rightSide = "yuiophjklbnm"

lx, ly, rx, ry = None, None, None, None

for i in range(len(keyboard)):
    if left in keyboard[i]:
        lx = i
        ly = keyboard[i].index(left)

    if right in keyboard[i]:
        rx = i
        ry = keyboard[i].index(right)

time = 0
for s in string:
    time += 1  # 각 키를 누르는 데에 1의 시간이 걸린다.
    if s in rightSide:
        for i in range(len(keyboard)):
            if s in keyboard[i]:
                nx = i
                ny = keyboard[i].index(s)

                time += abs(nx - rx) + abs(ny - ry)
                rx = nx
                ry = ny
                break
    else:
        for i in range(len(keyboard)):
            if s in keyboard[i]:
                nx = i
                ny = keyboard[i].index(s)

                time += abs(nx - lx) + abs(ny - ly)
                lx = nx
                ly = ny
                break

print(time)
