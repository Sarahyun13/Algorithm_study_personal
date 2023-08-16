for t in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    count = 0

    for i in range(2, N - 2):
        sideMax = max(
            building[i - 2], building[i - 1], building[i + 1], building[i + 2]
        )
        view = building[i] - sideMax
        if view > 0:
            count += view

    print("#{} {}".format(t, count))
