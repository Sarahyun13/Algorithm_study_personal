switchNum = int(input())
switchState = list(map(int, input().split()))
studentNum = int(input())

for _ in range(studentNum):
    s, n = map(int, input().split())

    if s == 1:
        for i in range(n-1, switchNum):
            if (i+1) % n == 0:
                switchState[i] = (switchState[i] + 1) % 2
    else:
        if n <= switchNum//2:
            count = n - 1
        else:
            count = switchNum - n

        for i in range(1, count+1):
            if switchState[n-1-i] == switchState[n-1+i]:
                switchState[n-1-i] = (switchState[n-1-i] + 1) % 2
                switchState[n-1+i] = (switchState[n-1+i] + 1) % 2
            else:
                break
        switchState[n-1] = (switchState[n-1] + 1) % 2

for i in range(1, switchNum+1):
    print(switchState[i-1], end=" ")
    if i % 20 == 0:
        print()