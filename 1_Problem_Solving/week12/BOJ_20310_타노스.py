import sys

input = sys.stdin.readline

s = input().strip()
s = list(s)
# print(s)

count0 = s.count("0") // 2
count1 = s.count("1") // 2

# 문자열의 순서를 유지하면서 절반을 없애햐 하기 때문에에
# 0은 뒤에서부터 제거
# print(s[::-1])
# print(-s[::-1].index("0"))
for _ in range(count0):
    s.pop(-s[::-1].index("0") - 1)

# 1은 앞에서부터 제거
for _ in range(count1):
    s.pop(s.index("1"))

# for i in s:
#     print(i, end="")
print("".join(s))
