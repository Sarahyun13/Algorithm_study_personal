import sys

input = sys.stdin.readline

first = int(input())

result = []
for second in range(1, first+1):
    nums = [first, second]
    while True:
        next = nums[-2] - nums[-1]
        if next < 0:
            if len(result) < len(nums):
                result = nums[:]
            break
        nums.append(next)

print(len(result))
print(*result)

