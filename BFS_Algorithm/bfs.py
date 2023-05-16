# 그래프 탐색 - 너비 우선 탐색(BFS: Breadth First Search)
# 시작 정점에서 인접한 노드를 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문
# 모든 노드를 탐색하는 것보다 최소 비용, 최단 경로, 임의의 경로를 찾아야 하는 경우에 사용
# 큐(Queue) 를 이용하여 구현
# 1. 시작 노드를 Queue에 삽입하고 visit[시작] = true 로 방문 처리
# 2. Queue의 front를 현재 노드 변수에 저장하고 pop()
# 3. Queue의 현재 노드에 방문하지 않은 인접 노드가 있다면 Queue에 삽입하고 방문 처리
# 4. Queue가 빌 때까지 반복

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # 현재 노드 방문 처리

    while queue: # 아직 큐에 노드가 있다면
        cur = queue.popleft() # 하나를 빼와 현재 노드 변수에 저장
        print(cur, end=' ') # 출력

        for next in graph[cur]: 
            if not visited[next]: # 방문하지 않은 노드라면
                queue.append(next) # 큐에 삽입
                visited[next] = True # 방문 처리


N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (N + 1)