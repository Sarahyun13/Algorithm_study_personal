import sys

input = sys.stdin.readline

doc = input().rstrip()
word = input().rstrip()

docIndex = 0
count = 0
while docIndex <= len(doc) - len(word):
    if doc[docIndex : docIndex + len(word)] == word:
        count += 1
        docIndex += len(word)
    else:
        docIndex += 1

print(count)
