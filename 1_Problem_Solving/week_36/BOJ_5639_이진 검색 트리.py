import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break


def post(start, end):
    if start > end:
        return
    # 루트보다 큰 값(오른쪽 서브 트리)이 존재하지 않을 경우를 대비해 초기화
    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:
            mid = i
            break

    post(start + 1, mid - 1)  # 왼쪽 서브 트리 탐색
    post(mid, end)  # 오른쪽 서브 트리 탐색
    print(pre[start])  # 루트 노드 출력


post(0, len(pre) - 1)
