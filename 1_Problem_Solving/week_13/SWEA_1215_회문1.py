for t in range(1, 11):
    leng = int(input())

    words = []
    for _ in range(8):
        words.append(list(input().rstrip()))

    count = 0
    # 가로
    for i in range(8):
        for j in range(8 - leng + 1):
            word = words[i][j : j + leng]
            if word == word[::-1]:
                count += 1

    # 세로
    for j in range(8):
        for i in range(8 - leng + 1):
            word = ""
            for k in range(i, i + leng):
                word += words[k][j]
            if word == word[::-1]:
                count += 1

    print("#{} {}".format(t, count))
