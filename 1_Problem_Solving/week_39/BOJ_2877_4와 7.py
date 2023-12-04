import sys

input = sys.stdin.readline

# k번째 수는 k+1을 이진수로 바꾸고, 가장 앞자리를 없앤 후,
# 0과 1을 다시 4와 7로 바꾸는 규칙
k = int(input())
binK = format(k + 1, "b")
binK = binK[1:]
print(binK.replace("0", "4").replace("1", "7"))

print(str(bin(k + 1)[3:]).replace("0", "4").replace("1", "7"))
