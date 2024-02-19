import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dna = []
for _ in range(N):
    dna.append(input().rstrip())

nucleo = ['A', 'C', 'G', 'T']
result = ''
hamming = 0
for i in range(M):
    count = [0, 0, 0, 0] # A, C, G, T의 개수
    # 입력 받은 dna들의 열 별로 가장 많이 나온 문자를 본다.
    for j in range(N):
        if dna[j][i] == nucleo[0]:
            count[0] += 1
        elif dna[j][i] == nucleo[1]:
            count[1] += 1
        elif dna[j][i] == nucleo[2]:
            count[2] += 1
        elif dna[j][i] == nucleo[3]:
            count[3] += 1

    result += nucleo[count.index(max(count))]
    hamming += N - max(count)

print(result)
print(hamming)