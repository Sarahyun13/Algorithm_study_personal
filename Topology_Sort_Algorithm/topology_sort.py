# Topology Sort Algorithm (위상 정렬 알고리즘)
# DAG(Direct Acyclic Graph == 비순환 방향 그래프)에 존재하는 각 정점들의 선행 순서를 위배하지 않으면서 모든 정점을 나열하는 것
# 위상 정렬의 대표적인 예로 대학교의 선수과목 구조를 들 수 있다.
# 예를 들어, 자료 구조를 수강하려면 먼저 이산 수학을 수강하여야 한다.
# 즉 선수 과목은 과목들의 선행 관계를 표현하게 된다.
# 위상 정렬은 진입 차수를 이용해 구현하는 알고리즘으로, 큐와 스택을 이용해 2가지 방법으로 구현할 수 있다.
# 위상 정렬의 시간 복잡도는 O(V + E)이다.
# 처음에 진입차수가 0이 되는 노드를 찾기 위해 선형적으로 탐색해서 O(V) 즉, 노드 총 개수만큼의 시간 복잡도
# 그리고 큐에서 뺀 노드와 연결된 간선 개수(E)만크 또 선형 탐색하므로 O(E)를 더해 총 시간 복잡도가 O(V + E)

# 1. 진입 차수가 0인 노드들을 큐에 삽입한다.
# 2. 큐에서 노드를 꺼내 해당 노드에 연결된 간선을 그래프에서 제거한다.
# 3. 새롭게 진입차수가 0이 된 노드들을 큐에 삽입한다.
# 4. 큐가 빌 때까지 위 1~3 과정을 반복한다.
# 진입 차수가 0인 정점이 여러 개 존재할 경우 어느 정점을 선택하여도 무방하다.
# 따라서, 하나의 그래프에는 복수의 위상 순서가 있을 수 있다.

# Queue(큐) 이용
from collections import deque

# 위상 정렬 함수
def topologySort():
    result = []
    q = deque()

    # 초기에 진입 차수가 0인 노드들 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        cur = q.popleft()
        result.append(cur) # 꺼낸 노드는 위상 정렬 결과 값에 삽입

        # 꺼낸 노드랑 연결된 노드들 탐색
        for node in graph[cur]:
            indegree[node] -= 1 # 연결된 노드들의 진입 차수 1 빼기
            if indegree[node] == 0: # 새롭게 진입 차수가 0이 되는 노드들
                q.append(node) # 큐에 삽입
    
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end = " ")


v, e = map(int, input().split()) # 노드와 간선 개수 입력 받기
indegree = [0] * (v + 1) # 모든 노드에 대한 진입 차수는 0으로 초기화
graph = [[] for _ in range(v + 1)] # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화

# 방향 그래프의 모든 간선 정보 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 a에서 b로 이동 가능 (a->b)
    indegree[b] += 1 # b의 진입 차수를 1 증가시킴

topologySort()