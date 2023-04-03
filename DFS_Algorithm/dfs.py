# 그래프 탐색 - 깊이 우선 탐색(DFS: Depth First Search)
# 시작 정점에서 한 방향으로 계속 내려 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 올라와서 다른 방향으로 내려가며 탐색 진행
# 모든 노드를 방문해야 하는 경우에 사용
# 스택(Stack) 또는 재귀함수를 이용하여 구현

# 재귀함수 사용
# 1. 현재 노드 방문 처리
# 2. 현재 노드와 인접한 노드들 중 방문한 적 없는 노드가 있다면 재귀 호출
def recursiveDfs(graph, start, visited):
    visited[start] = True # 방문 표시
    print(start, end = " ")

    for next in graph[start]:
        if not visited[next]: # 방문한 적 없는 노드라면
            recursiveDfs(graph, next, visited) # 재귀 호출

# Stack 사용
# 1. 시작 노드를 Stack에 삽입하고 visit[시작] = true 로 방문 처리
# 2. Stack의 최상단 노드 top을 현재 노드 변수에 저장하고 pop() 하고 방문 처리
# 3. Stack의 현재 노드에 방문하지 않은 인접 노드가 있다면 Stack에 삽입
# 4. Stack이 빌 때까지 반복
def stackDfs(graph, start, visited):
    stack = [start] # Stack에 삽입
    
    while stack: # 아직 Stack에 노드가 있다면
        cur = stack.pop() # 최상단 노드 현재 변수에 저장하고 Stack에서 제거

        if not visited[cur]: # 방문하지 않은 노드라면
            print(cur, end = " ")
            visited[cur] = True # 방문 처리
            for next in graph[cur]:
                stack.append(next) # 인접 노드들 Stack에 삽입

