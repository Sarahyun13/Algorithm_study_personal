for t in range(1, 11):
    dump = int(input())

    box = list(map(int, input().split()))

    gap = 0
    while dump > 0:
        big = box.index(max(box))
        small = box.index(min(box))
        gap = box[big] - box[small]

        if gap <= 1:
            break
        else:
            box[big] -= 1
            box[small] += 1
            dump -= 1

    gap = max(box) - min(box)
    print("#{} {}".format(t, gap))
