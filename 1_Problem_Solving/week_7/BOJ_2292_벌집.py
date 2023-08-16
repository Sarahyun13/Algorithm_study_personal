n = int(input())
count = 1
sum = 1

while sum < n:
    sum = sum + count * 6
    count += 1

print(count)