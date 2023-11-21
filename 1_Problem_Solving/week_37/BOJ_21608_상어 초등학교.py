import sys

input = sys.stdin.readline

# 1. 인접한 칸에 좋아하는 학생이 가장 많은 빈 칸
# 2. 인접한 칸이 비어있는 경우가 가장 많은 빈 칸
# 3. 행의 번호가 가장 작은 칸
# 4. 열의 번호가 가장 작은 칸

N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
seats = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for k in range(N**2):
    student = students[k]  # 현재 학생과 학생이 좋아하는 학생들
    result = []  # 현재 학생을 앉힐 수 있는 자리 후보 리스트

    for x in range(N):
        for y in range(N):
            if seats[x][y] == 0:  # 빈 자리일 경우에만
                like = 0  # 인접한 칸들 중 좋아하는 학생들이 있는 칸 수
                empty = 0  # 인접한 칸들 중 빈 칸 수
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if seats[nx][ny] in student[1:]:  # 인접 칸에 좋아하는 학생이 있다면
                            like += 1
                        if seats[nx][ny] == 0:  # 인접 칸이 빈 칸이라면
                            empty += 1
                # 자리 후보 리스트에 고려사항 우선순위대로 한꺼번에 리스트로 추가
                result.append([like, empty, x, y])

    # 후보 칸들을 like, empty는 내림차순, 행과 열은 오름차순으로 정렬
    result.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    # 정렬 후, 맨 앞에 있는 리스트의 행과 열의 자리에 학생 앉히기
    seats[result[0][2]][result[0][3]] = student[0]

# 만족도를 구할 때는 학생의 번호 순서대로 점수를 구할 수 있도록 정렬
students.sort()
answer = 0
for x in range(N):
    for y in range(N):
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < N
                and (seats[nx][ny] in students[seats[x][y] - 1])
            ):
                count += 1

        if count != 0:
            answer += 10 ** (count - 1)

print(answer)
