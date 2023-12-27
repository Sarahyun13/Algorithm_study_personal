import sys

input = sys.stdin.readline
trees = dict()
count = 0
while True:
    tree = input().rstrip()
    if not tree:
        break

    count += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

treesList = list(trees.keys())
treesList.sort()
for tree in treesList:
    ratio = trees[tree] / count * 100
    print("%s %.4f" % (tree, ratio))
