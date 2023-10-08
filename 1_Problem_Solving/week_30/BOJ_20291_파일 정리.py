import sys

input = sys.stdin.readline

N = int(input())
files = [input().rstrip() for _ in range(N)]

extension = {}
for i in range(len(files)):
    name = files[i][files[i].index(".") + 1 :]
    # print(name)
    if name not in extension:
        extension[name] = 1
    else:
        extension[name] += 1

# print(extension)
extension = dict(sorted(extension.items()))
# print(extension)
for key, val in extension.items():
    print(key, val)
