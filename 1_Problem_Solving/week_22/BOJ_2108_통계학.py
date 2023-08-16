import sys

input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()

count = dict()
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

maxCount = []
for key in count:
    if count[key] == max(count.values()):
        maxCount.append(key)

print(round(sum(nums) / N))
print(nums[N // 2])
if len(maxCount) == 1:
    print(maxCount[0])
else:
    print(maxCount[1])
print(max(nums) - min(nums))
