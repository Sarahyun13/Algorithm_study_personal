import sys

input = sys.stdin.readline


def find(start):
    global count
    j = 0
    first = True
    for i in range(start, len(sound)):
        if sound[i] == quack[j] and not visited[i]:
            visited[i] = 1
            if sound[i] == "k":
                # 오리가 여러 번 울어도 한 마리가 운 거기 때문에 처음에만 count함
                if first:
                    count += 1
                    first = False  # 오리의 첫 울음소리만 세면 되므로, 다음에 나오는 울음소리들은 count에 안 더하기 위해
                j = 0  # 마지막 문자인 k까지 나왔으면 다시 q부터 찾아서 비교해야 함
            else:
                j += 1  # 다음 문자 고려


sound = input().rstrip()
visited = [False] * len(sound)
quack = "quack"

# 입력받은 녹음 소리가 5('quack'길이)의 배수가 아니라면 올바르지 않은 울음 소리
if len(sound) % 5 != 0:
    print(-1)
    exit()

count = 0  # 오리의 수
for i in range(len(sound)):
    if sound[i] == "q" and not visited[i]:
        find(i)

# 오리의 수가 0이거나 모든 소리를 방문하지 않았을 경우
if count == 0 or not all(visited):
    print(-1)  # 올바르지 않은 소리
else:  # 올바른 소리일 경우
    print(count)  # 오리의 수 출력
