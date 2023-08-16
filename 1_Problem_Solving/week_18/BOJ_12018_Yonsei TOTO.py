import sys

input = sys.stdin.readline

n, m = map(int, input().split())

subject = []
for _ in range(n):
    enroll, limit = map(int, input().split())
    mil = list(map(int, input().split()))
    mil.sort(reverse=True)

    # 신청 인원이 수강 정원보다 적다면
    if enroll < limit:
        # 마일리지를 1점만 써도 수강 가능하므로 과목 리스트에 1점으로 추가
        subject.append(1)
    # 신청 인원이 수강 정원보다 많다면
    else:
        # 수강 정원번째 마일리지 수만큼만 사용하면 되므로 과목 리스트에 사용할 마일리지 추가
        subject.append(mil[limit - 1])

# 과목 개수를 최대로 만들어야 하므로 오름차순 정렬
subject.sort()
count = 0
# 마일리지 수가 적은 과목부터 수강 신청
for point in subject:
    if point <= m:
        count += 1
        m -= point
    else:
        break

print(count)
