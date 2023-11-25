import sys

input = sys.stdin.readline

# 리스트를 활용하여 풀면 시간 초과
# 동명이인이 존재할 수 있다는 점 유의
# 딕셔너리는 key 값이 일치하면 다 한 번에 삭제하므로
# 동명이인이라면 value 값을 1 증가시키는 방식으로 해결한다.

N = int(input())

people = dict()
for _ in range(N):
    name = input().rstrip()
    if name in people:  # 같은 이름이 이미 존재한다면
        people[name] += 1  # value 값 1 증가시킨다.
    else:  # 새로운 이름이라면
        people[name] = 1  # key, value 새로 생성

for _ in range(N - 1):
    person = input().rstrip()
    people[person] -= 1  # 완주한 사람 value 값 1 감소시킨다.

for person in people:
    if people[person]:  # key에 해당하는 value 값이 1이라면
        print(person)  # 완주하지 못한 사람
        break
