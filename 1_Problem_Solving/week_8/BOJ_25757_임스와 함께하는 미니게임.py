# 추가해야 시간 초과 안 남;;
import sys
input = sys.stdin.readline

n, game = input().split()
n = int(n)

'''
# 그냥 리스트로 구현
applyList = []
for i in range(n):
    name = input()
    if name in applyList: continue
    
    applyList.append(name)

if game == 'Y':
    print(len(applyList))
elif game == 'F':
    print(len(applyList) // 2)
elif game == 'O':
    print(len(applyList) // 3)
'''

# 집합으로 구현
applyList = set()
for i in range(n):
    name = input()
    applyList.add(name)

if game == 'Y':
    print(len(applyList))
elif game == 'F':
    print(len(applyList) // 2)
elif game == 'O':
    print(len(applyList) // 3)