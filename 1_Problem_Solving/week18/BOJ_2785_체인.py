import sys

input = sys.stdin.readline

N = int(input())
chain = list(map(int, input().split()))

# 연결된 고리가 제일 적은 체인을 소모하는 것이 체인을 최소로 사용하여 모든 체인을 연결할 수 있는 방법.
chain.sort()  # 정렬
count = 0
ring = N - 1
i = 0
while ring > 0:
    if chain[i] < ring:
        count += chain[i]
        ring -= 1
        ring -= chain[i]
    elif chain[i] >= ring:
        count += ring
        ring = 0

    i += 1

print(count)
