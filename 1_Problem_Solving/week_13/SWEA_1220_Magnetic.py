for t in range(1, 11):
    n = int(input())
    table = []
    for _ in range(100):
        table.append(list(map(int, input().split())))

    count = 0
    for j in range(100):
        check = False
        for i in range(100):
            if table[i][j] == 1:
                check = True
            elif table[i][j] == 2 and check:
                count += 1
                check = False

    print("#{} {}".format(t, count))
