def cutPaper(r, c, n):
    global minusCount, zeroCount, plusCount

    num = paper[r][c]
    # 종이의 각 칸의 숫자 확인
    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper[i][j] != num: # 종이가 모두 같은 수로 되어 있는 것이 아니라면
                for k in range(3):
                    for l in range(3):
                        cutPaper(r+k*(n//3), c+l*(n//3), n//3) # 3 * 3 으로 재귀 탐색
                return
            
    if num == -1: minusCount += 1
    elif num == 0: zeroCount += 1
    elif num == 1: plusCount +=1

n = int(input())

# 행렬 입력 받기
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

minusCount = 0
zeroCount = 0
plusCount = 0

cutPaper(0, 0, n)
print(minusCount, zeroCount, plusCount, sep='\n')