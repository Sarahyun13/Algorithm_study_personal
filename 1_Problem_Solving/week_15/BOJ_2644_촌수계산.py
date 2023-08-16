import sys

input = sys.stdin.readline


def dfs(num):
    for next in family[num]:
        if visited[next] == 0:  # 방문하지 않았다면
            visited[next] = visited[num] + 1  # 누적
            dfs(next)


n = int(input())  # 전체 사람 수
num1, num2 = map(int, input().split())  # 촌수를 계산해야 하는 두 사람
m = int(input())  # 부모 자식들 간의 관계 개수

family = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    # 무방향 그래프처럼 연결된 관계 양쪽으로 다 삽입하여 저장
    family[x].append(y)
    family[y].append(x)

visited = [0] * (n + 1)
dfs(num1)

if visited[num2] > 0:  # 친척 관계가 있다면
    print(visited[num2])
else:  # 친척 관계가 전혀 없다면
    print(-1)
