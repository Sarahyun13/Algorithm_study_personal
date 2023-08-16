n, k = map(int, input().split())

country = []
for i in range(n):
    country.append(list(map(int, input().split())))

# 두 번째 값(금메달)이 같을 경우, 세 번째 값(은메달)
# 세 번째 값(은메달)도 같을 경우, 네 번째 값(동메달)
# 기준으로 내림차순 정렬
country.sort(key=lambda x:(-x[1], -x[2], -x[3]))
# country.sort(key=lambda x: (x[1], x[2], x[3]), reverse = True)

# k 국가의 index 값을 찾는다
for i in range(n):
    if country[i][0] == k:
        index = i

# 등수가 같은 나라가 있을 때를 대비해서 for문을 돌며
# 국가 k의 금, 은, 동메달 수와 같은 국가가 나오면
# index는 0부터 시작하고 등수는 1부터 시작하므로
# 그 국가의 (index+1)등이므로 출력하고 break
for i in range(n):
    if country[index][1:] == country[i][1:]:
        print(i+1)
        break