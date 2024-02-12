import sys

input = sys.stdin.readline

def dfs():
    global result

    if len(arr) == N:
        temp = 0
        for i in range(N-1):
            temp += abs(arr[i]-arr[i+1])
        result = max(result, temp)
        return

    for i in range(N):
        if not visited[i]:
            arr.append(A[i])
            visited[i] = True
            dfs()
            arr.pop()
            visited[i] = False

N = int(input())
A = list(map(int, input().split()))

arr = []
# 주어진 배열에 같은 숫자가 있을 경우를 대비해 방문 여부 확인 가능한 배열 따로 사용
visited = [False] * N
result = 0
dfs()
print(result)