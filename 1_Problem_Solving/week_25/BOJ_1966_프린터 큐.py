import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # enumerate 이용해서 인덱스와 중요도 함께 저장 가능
    docs = list(enumerate(list(map(int, input().split()))))
    target = docs[M]
    count = 0
    while len(docs):
        maxDoc = max(docs, key=lambda x: x[1])
        if docs[0] == maxDoc:
            doc = docs.pop(0)
            count += 1

            if doc == target:
                print(count)
                break
        else:
            docs.append(docs.pop(0))
