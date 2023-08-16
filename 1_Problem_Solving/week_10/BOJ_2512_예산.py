import sys
input = sys.stdin.readline

N = int(input())
budget = list(map(int, input().split()))
M = int(input())

start, end = 0, max(budget)

# 이분 탐색
if sum(budget) <= M:
    print(max(budget))
else:
    while start <= end:
        mid = (start+end)//2
        total = 0 # 총 지출

        for money in budget:
            if money > mid:
                total += mid
            else:
                total += money
        
        if total <= M: # 총 지출이 예산보다 적으면
            start = mid+1
        else: # 총 지출이 예산보다 크면
            end = mid-1
    
    print(end)
