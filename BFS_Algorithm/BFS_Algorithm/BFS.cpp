// 그래프 탐색 - 너비 우선 탐색(BFS: Breadth First Search)
// 시작 정점에서 인접한 노드를 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문
// 모든 노드를 탐색하는 것보다 최소 비용, 최단 경로, 임의의 경로를 찾아야 하는 경우에 사용
// 큐(Queue) 를 이용하여 구현
// 1. 시작 노드를 Queue에 삽입하고 visit[시작] = true 로 방문 처리
// 2. Queue의 front를 현재 노드 변수에 저장하고 pop()
// 3. Queue의 현재 노드에 방문하지 않은 인접 노드가 있다면 Queue에 삽입하고 방문 처리
// 4. Queue가 빌 때까지 반복

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX_SIZE 1000

using namespace std;

vector <int> graph[MAX_SIZE];
bool visit[MAX_SIZE]; // 전역으로 선언하면 false로 자동 초기화

void bfs(int start) {
	queue<int> q;

	q.push(start); // Queue에 시작 노드 삽입하고
	visit[start] = true; // 방문 처리

	while (!q.empty()) { // 아직 Queue에 노드가 있다면
		int now = q.front(); // front를 현재 노드 변수에 저장
		q.pop(); // Queue에서 제거
		cout << now << " ";

		for (int i = 0; i < graph[now].size(); i++) {
			int next = graph[now][i];
			if (!visit[next]) { // 방문하지 않은 노드라면
				q.push(graph[now][i]); // Queue에 삽입
				visit[next] = true; // 방문 처리
			}
		}
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

	bfs(start);

	return 0;
}