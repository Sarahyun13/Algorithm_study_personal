import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

count = 0
for i in range(len(nums)):
    prime = True

    if nums[i] < 2:  # 2보다 작으면
        prime = False  # 소수가 아님
    elif nums[i] == 2:  # 2이면
        count += 1  # 소수
    elif nums[i] > 2:  # 2보다 크면
        for k in range(2, nums[i]):  # 2 이상이며 자기 자신보다 작은 모든 수들로 나눠 본다
            if nums[i] % k == 0:  # 나누어 떨어지는 수가 있다면 약수가 존재하는 것이므로
                prime = False  # 소수가 아님
                break
        if prime:
            count += 1

print(count)
