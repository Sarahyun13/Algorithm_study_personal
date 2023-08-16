T = int(input())

for _ in range(T):
    N = int(input())
    table = list(map(int, input().split()))
    count = {} # 팀당 주자 수

    # 팀별로 주자 수 세기
    for i in range(N):
        if table[i] in count:
            count[table[i]] += 1
        else:
            count[table[i]] = 1

    # 제외되는 팀 구하기
    dele = [] # 제외되는 팀
    for key, val in count.items():
        if val < 6:
            dele.append(key)

    # 점수 계산
    team = {}
    score = 1 # 점수
    for i in range(N):
        if table[i] not in dele: # 제외 리스트에 없고,
            if table[i] in team: # 팀테이블에 이미 존재하고,
                if team[table[i]][0] < 4: # 포함된 상위 주자 수가 4 미만이라면
                    team[table[i]][0] += 1 # 상위 4명 주자 수에 한 명 추가
                    team[table[i]][1] += score # 상위 4명 점수 합에 점수 더함
                elif team[table[i]][0] == 4:
                    team[table[i]][0] += 1
                    team[table[i]][2] = score

            else:
                            # 팀당 주자 수, 상위 4명 점수 합, 5번째 주자의 점수
                team[table[i]] = [1, score, 0]

            score += 1
    
    # 순위 정렬
    team = sorted(team.items(), key=lambda x:(x[1][1], x[1][2]))
    #print(team)
    print(team[0][0])
