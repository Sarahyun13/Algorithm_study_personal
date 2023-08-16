def dfs(count):
    global answer

    if count == changeNum:  # 최대 교환 횟수에 도달하면
        temp = "".join(numbers)  # 문자열 반환
        answer = max(answer, temp)
        return

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # 하나씩 교환
            numbers[i], numbers[j] = numbers[j], numbers[i]
            temp = "".join(numbers)

            # 방문 확인 -> 시간 초과 방지
            if visited.get((temp, count), 1):  # visited에 (temp, count)라는 key가 존재하지 않으면
                visited[(temp, count)] = 0
                dfs(count + 1)

            # dfs 수행이 종료되었다면 다른 경로의 dfs 수행을 위해 num 원상 복구
            numbers[i], numbers[j] = numbers[j], numbers[i]


test = int(input())

for t in range(1, test + 1):
    numbers, changeNum = input().split()
    numbers = list(numbers)
    changeNum = int(changeNum)

    answer = "0"
    visited = {}
    dfs(0)
    print("#{} {}".format(t, answer))
