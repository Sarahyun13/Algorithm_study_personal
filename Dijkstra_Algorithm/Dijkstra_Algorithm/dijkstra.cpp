// 하나의 시작 정점으로부터 모든 다른 정점까지의 <최단 경로>를 찾는 알고리즘
// 음이 아닌 가중 그래프에서의 단일 쌍, 단일 출발, 단일 도착 최단 경로 문제
// 1. dist 배열 INF로 초기화
// 2. 시작점 입력 받고, dist[시작점]=0, visit[시작점]=true 로 설정 (탐색 방법)
//		시작점 입력 받고, dist[시작점]=0, pq에 {0, 시작점} 삽입 (우선순위 큐 방법)
// 3. dist 배열에서 최소 비용 정점을 찾고 visit 처리, 이미 방문한 노드는 제외. (탐색 방법)
//		pq.empty() 될 때까지 (우선순위 큐 방법)
//		-> pq.front() = {거리 비용, 노드 인덱스}
//		-> dist[노드 인덱스] < 거리 비용 이면 이미 체크한 경우이므로 패스
// 4. 새로운 정점을 거쳐 갈 수 있는 거리가 기존 거리보다 작다면 거리값 갱신

#include <iostream>
#include <vector>
#include <queue>
#define INF 99999
#define MAX_SIZE 100

using namespace std;

vector<vector<int>> weight; // 가중치 그래프
int dist[MAX_SIZE]; // 시작 정점으로부터의 최단 거리
bool visit[MAX_SIZE]; // 방문한 정점 표시
int v, e, start;

// 1. 우선순위 큐 사용하지 않고 직접 탐색하는 방법 (시간복잡도는 O(V^2))
int getSmallestNode() { // 방문하지 않은 노드들 중에서 가장 최소 비용의 노드 반환
	int min = INF;
	int index = 0;

	for (int i = 0; i < v; i++) {
		if (!visit[i]) { // 방문하지 않았고
			if (dist[i] < min) { // 가장 작은 값 구하기
				min = dist[i];
				index = i;
			}
		}
	}

	return index;
}

void dijkstra1(int start) {
	for (int i = 0; i < v; i++) {
		dist[i] = weight[start][i]; // 시작점부터 모든 정점까지의 최단거리 초기값 설정
	}
	dist[start] = 0;
	visit[start] = true;

	for (int i = 0; i < v - 1; i++) { // 시작점을 제외한 모든 정점 방문
		int now = getSmallestNode();
		visit[now] = true;

		for (int j = 0; j < v; j++) {
			if (!visit[j]) { // 방문하지 않았고
				int cost = dist[now] + weight[now][j];
				if (cost < dist[j]) dist[j] = cost; // 새로운 정점을 거쳐가는 게 더 작으면 값 갱신
			}
		}
	}

}

// 2. 우선순위 큐(최소 힙)를 사용하는 방법 (시간복잡도는 O(ElogE)) -> 더 빠름
//		우선순위 큐의 디폴트가 내림차순 정렬이기 때문에 거리 비용을 음수로 변환해서 저장 -> 오름차순 정렬처럼 보이게
void dijkstra2(int start) {
	priority_queue<pair<int, int>> pq; // <거리, 정점 인덱스>
	pq.push({ 0, start }); // 시작 노드의 최단 거리 0으로 설정해서 큐에 삽입
	dist[start] = 0; // 시작 노드의 dist는 0으로 설정

	while (!pq.empty()) {
		int nowCost = -pq.top().first; // 저장된 음수에 - 붙여서 양수로 변환해서 가져옴
		int nowNode = pq.top().second;
		pq.pop();

		if (dist[nowNode] < nowCost) continue; // 이미 체크한 경우이므로 패스

		for (int i = 0; i < weight[nowNode].size(); i++) {
			int cost = nowCost + weight[nowNode][i];
			if (cost < dist[i]) { 
				dist[i] = cost; // 새로운 정점을 거쳐서 가는 게 더 작으면 값 갱신
				pq.push({ -cost, i }); // - 붙여서 음수로 변환해서 저장
			}
		}
	}
}

int main() {
	cout << "How many vertex?\n";
	cin >> v; // 정점 개수 입력

	weight.resize(v, vector<int>(v, INF));

	cout << "How many edge?\n";
	cin >> e; // 간선 개수 입력
	for (int i = 0; i < e; i++) {
		int from, to, cost;
		cin >> from >> to >> cost; // 정점 2개와 간선 입력(a에서 b로 가는 거리 비용 c)
		weight[from][to] = cost;
	}
	
	fill_n(dist, v, INF); // 최단 거리 배열 INF로 초기화

	cout << "Start node?\n";
	cin >> start; // 시작 노드 입력

	//dijkstra1(start);

	dijkstra2(start);

	for (int i = 0; i < v; i++) {
		cout << dist[i] << " ";
	}

	return 0;
}