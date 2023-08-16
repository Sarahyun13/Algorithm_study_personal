testNum = int(input())

for t in range(1, testNum + 1):
    N = int(input())
    letter = list(map(int, input().split()))
    visited = [False] * (N + 1)
    count = 0

    for i in range(N):
        if not visited[i]:
            val = letter[i]
            if 0 <= i + val < N and (val + letter[i + val]) == 0:
                count += 1
                visited[i] = True
                visited[i + val] = True

    print("#{} {}".format(t, count))
