import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(cur):
    count = 0

    # 다리로 연결된 섬들을 탐색하며 결과 값에 더해준다.
    for next in islands[cur]:
        count += dfs(next)

    if island[cur][0] == 'W': # 현재 섬에 늑대가 있다면
        count -= island[cur][1] # 넘어온 양을 잡아 먹는다.
        if count < 0: # 살아 남은 양이 없거나 늑대만 있다면
            count = 0 # 늑대는 넘어갈 수 없으니 0을 넘겨 준다.
    else: # 현재 섬에 양이 있다면
        count += island[cur][1] # 양의 수를 넘겨 준다.

    return count

N = int(input())
islands = [[] for _ in range(N+1)]
island = [[], [0, 0]]
for i in range(2, N+1):
    animal, number, connect = input().rstrip().split()
    island.append([animal, int(number)])  # 섬의 정보
    islands[int(connect)].append(i) # 다리로 연결된 섬들

print(dfs(1))