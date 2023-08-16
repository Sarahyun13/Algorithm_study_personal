import sys

input = sys.stdin.readline


def palindrome(word, l, r):
    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            leftRemove = check(word, l + 1, r)  # 왼쪽 문자 하나 제거
            rightRemove = check(word, l, r - 1)  # 오른쪽 문자 하나 제거
            if leftRemove or rightRemove:
                return 1
            else:
                return 2
    return 0


def check(word, l, r):
    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            return False

    return True


T = int(input())
for _ in range(T):
    word = input().rstrip()
    print(palindrome(word, 0, len(word) - 1))
