# h행 w열 세로로 n, 가로로 m만큼의 차
h, w, n, m = map(int, input().split())

# 한 행에 들어갈 수 있는 인원 수
i = h // (n+1)
if(h % (n+1) != 0):
    i += 1

# 한 열에 들어갈 수 있는 인원 수
j = w // (m+1)
if(w % (m+1) != 0):
    j += 1

# 강의실 수용 최대 인원 수
result = i * j
print(result)