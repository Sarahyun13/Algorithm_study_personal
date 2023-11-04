import sys

input = sys.stdin.readline

N = int(input())
shortcut = []
for _ in range(N):
    option = list(input().rstrip().split())

    find = False
    for idx, word in enumerate(option):
        if word[0].upper() not in shortcut:
            shortcut.append(word[0].upper())
            word = "[" + word[0] + "]" + word[1:]
            option[idx] = word
            find = True
            break

    if not find:
        for idx, word in enumerate(option):
            for i in range(len(word)):
                if word[i].upper() not in shortcut:
                    shortcut.append(word[i].upper())
                    word = word[:i] + "[" + word[i] + "]" + word[i + 1 :]
                    option[idx] = word
                    find = True
                    break
            if find:
                break

    print(" ".join(option))

# print(shortcut)
