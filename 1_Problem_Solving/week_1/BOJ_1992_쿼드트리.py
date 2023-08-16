def compress(r, c, n):
    num = video[r][c]

    for i in range(r, r+n):
        for j in range(c, c+n):
            if video[i][j] != num: # 같은 수로 되어 있지 않다면
                print('(', end='')
                n = n//2
                compress(r, c, n) # 왼쪽 위
                compress(r, c+n, n) # 오른쪽 위
                compress(r+n, c, n) # 왼쪽 아래
                compress(r+n, c+n, n) # 오른쪽 아래
                print(')', end='')
                return
            
    if num == 1:
        print(1, end='')
    elif num == 0:
        print(0, end='')

n = int(input())

# 행렬 입력 받기
# video = [list(map(int, input())) for _ in range(n)]
video = []
for i in range(n):
    video.append(list(map(int, input())))

compress(0, 0, n)