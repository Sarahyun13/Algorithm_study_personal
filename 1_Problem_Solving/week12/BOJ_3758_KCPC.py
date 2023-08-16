import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # n: 팀 개수, k: 문제 개수, t: 내 팀 ID, m: 로그 엔트리 개수
    n, k, t, m = map(int, input().split())
    score = [[0] * k for _ in range(n)]  # 문제와 점수
    count = [0] * n  # 제출 횟수
    time = [0] * n  # 제출 시간

    for seq in range(m):
        # i: 팀 ID, j: 문제 번호, s: 획득한 점수
        i, j, s = map(int, input().split())

        score[i - 1][j - 1] = max(score[i - 1][j - 1], s)
        count[i - 1] += 1
        time[i - 1] = seq

    result = []
    for idx in range(len(score)):
        # 최종 점수, 제출 횟수, 제출 시간, 팀 ID
        result.append([sum(score[idx]), count[idx], time[idx], idx])

    result.sort(key=lambda x: (-x[0], x[1], x[2]))

    for idx in range(len(result)):
        if result[idx][3] == t - 1:
            print(idx + 1)
            break
