import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

# 전위 순회에서 탐색한 루트 값을 기준으로 중위 순회에서는 왼쪽 서브 트리, 오른쪽 서브 트리로 분리된다.
# 전위 순회의 부모 값이 중위 순회의 값과 같을 때를 기점으로 중위 순회에서 왼쪽과 오른쪽으로 나눈다.
def postorder(root, start, end):
    for i in range(start, end):
        if preorder[root] == inorder[i]:
            postorder(root+1, start, i) # inorder(중위 순회)의 왼쪽 부분
            postorder(root+1+(i-start), i+1, end) # inorder(중위 순회)의 오른쪽 부분
            answer.append(preorder[root])

T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    answer = []
    postorder(0, 0, n)
    print(*answer)
