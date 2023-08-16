import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, team):
    visited[x] = 1  # 방문했음을 표시
    cycle.append(x)  # 사이클 리스트에 포함시킴
    nx = students[x]  # 다음에 방문할 곳

    if visited[nx] == 1:  # 방문한 적이 있는 곳이라면
        if nx in cycle:  # 사이클 가능 여부 확인
            # 사이클 되는 구간부터만 팀을 형성하므로 사이클 구간을 팀 리스트에 추가
            team += cycle[cycle.index(nx) :]
        return
    else:
        dfs(nx, team)

    return 0


T = int(input())

for _ in range(T):
    n = int(input())
    # 맨 앞에 0을 추가해 인덱스 접근이 쉽게 학생 리스트 생성
    students = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)  # 방문 여부

    team = []  # 팀을 구성한 학생들을 담는 리스트
    for i in range(1, n + 1):
        if visited[i] == 0:
            cycle = []  # 사이클을 확인하기 위한 리스트
            dfs(i, team)

    print(n - len(team))  # 팀에 속하지 못한 학생들의 수 출력
