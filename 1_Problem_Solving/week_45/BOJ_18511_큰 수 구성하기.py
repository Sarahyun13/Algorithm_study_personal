import sys
from itertools import product

input = sys.stdin.readline

N, K = map(int, input().split())
length = len(str(N))
setK = list(map(int, input().split()))
setK.sort(reverse=True) # 큰 수부터

# 단순 구현으로 풀면 시간 초과 난다.
# product 함수를 사용하여 집합 K의 숫자들을 이용해서 중복순열을 구할 수 있다.
# 만약 길이가 length인 모든 경우의 수 중에서 N보다 작은 수가 존재하지 않는다면,
# length를 1만큼 감소시켜서 위 과정을 반복한다.
while True:
    prod = list(product(setK, repeat=length))
    for n in prod:
        num = int(''.join(map(str, n)))
        if num <= N:
            print(num)
            exit()
    length -= 1
