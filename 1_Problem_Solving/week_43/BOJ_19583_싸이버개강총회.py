import sys

input = sys.stdin.readline

S, E, Q = input().rstrip().split()
attendance = set()
count = 0
while True:
    try:
        time, name = input().rstrip().split()
        if time <= S:
            attendance.add(name)
            # print(attendance)
        elif E <= time <= Q and name in attendance:
            attendance.remove(name)
            count += 1
    except:
        break

# print(attendance)
print(count)
