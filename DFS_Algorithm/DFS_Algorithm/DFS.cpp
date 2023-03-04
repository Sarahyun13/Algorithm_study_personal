// 그래프 탐색 - 깊이 우선 탐색(DFS: Depth First Search)
// 시작 정점에서 한 방향으로 계속 내려 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 올라와서 다른 방향으로 내려가며 탐색 진행
// 모든 노드를 방문해야 하는 경우에 사용
// 스택(Stack) 또는 재귀함수를 이용하여 구현

#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#define MAX_SIZE 1000

using namespace std;

vector <int> graph[MAX_SIZE];
bool visit[MAX_SIZE]; // 전역으로 선언하면 false로 자동 초기화

// Stack 사용
// 1. 시작 노드를 Stack에 삽입하고 visit[시작] = true 로 방문 처리
// 2. Stack의 최상단 노드 top을 현재 노드 변수에 저장하고 pop() 하고 방문 처리
// 3. Stack의 현재 노드에 방문하지 않은 인접 노드가 있다면 Stack에 삽입
// 4. Stack이 빌 때까지 반복
void dfs1(int start) {
	stack<int> st;

	st.push(start); // Stack에 삽입
	while (!st.empty()) { // 아직 Stack에 노드가 있다면
		int now = st.top(); // 최상단 노드 현재 변수에 저장
		st.pop(); // Stack에서 제거

		if (!visit[now]) { // 방문하지 않은 노드라면
			cout << now << " ";
			visit[now] = true; // 방문 처리

			for (int i = 0; i < graph[now].size(); i++) {
				st.push(graph[now][i]); // 인접 노드들 Stack에 삽입
			}
		}
	}
}

// 재귀함수 사용
// 1. 현재 노드 방문 처리
// 2. 현재 노드와 인접한 노드들 중 방문한 적 없는 노드가 있다면 재귀 호출
void dfs2(int start) {
	visit[start] = true; // 방문 표시
	cout << start << " ";

	for (int i = 0; i < graph[start].size(); i++) {
		int next = graph[start][i];
		if(!visit[next]) dfs2(next); // 방문한 적 없는 노드라면 재귀 호출
	}
}

int main() {
	int v, e, start;

	cout << "How many vertex?\n";
	cin >> v;

	cout << "How many edge?\n";
	cin >> e;

	cout << "Enter the start node\n";
	cin >> start;

	for (int i = 0; i < e; i++) {
		int v1, v2;
		cin >> v1 >> v2;

		graph[v1].push_back(v2);
		graph[v2].push_back(v1);
	}

	//dfs1(start);

	dfs2(start);

	return 0;
}
