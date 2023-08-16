p = int(input())

for n in range(p):
    kids = list(map(int, input().split()))
    t = kids.pop(0)
    count = 0

    for i in range(len(kids)-1):
        for j in range(i+1, len(kids)):
            if kids[i] > kids[j]:
                #kids[i], kids[j] = kids[j], kids[i] -> 자리 바꾸기 가능
                temp = kids[i]
                kids[i] = kids[j]
                kids[j] = temp
                count += 1
    
    print(t, count)