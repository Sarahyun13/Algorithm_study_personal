# DFS를 활용하여 폐업하지 않는 치킨 집을 조합으로 골라내어 품
# python의 itertools.combinations 사용해서 풀이 가능
# 주어지는 지도를 통해 치킨 집과 집의 좌표를 각 배열에 저장
# DFS로 치킨집 조합
# -> 치킨 집의 수가 m이 된다면 모든 집들의 치킨 집과의 최소 거리를 더하고
#       치킨 배달 거리를 구한다면 최소인지 확인하여 최소라면 업데이트

# dfs + 조합
def dfs(cur, chickenList):
    global chickenLen

    if len(chickenList) == m:
        length = 0
        for house in houses:
            houseLen = 1e9
            for c in chickenList:
                houseLen = min(houseLen, abs(house[0]-c[0]) + abs(house[1]-c[1]))
            length += houseLen
        
        chickenLen = min(chickenLen, length)
        return
    
    if cur == len(chickens):
        return
    
    # 현재 depth의 값 포함 재귀 호출
    dfs(cur+1, chickenList + [chickens[cur]])
    # 현재 depth의 값 미포함 재귀 호출
    dfs(cur+1, chickenList)

# 메인
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []
chickenList = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

chickenLen = 1e9
dfs(0, chickenList)
print(chickenLen)