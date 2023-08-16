word = input()
word = word.upper() # 다 대문자로 변경

alphabet = [0] * 26
for i in range(len(word)):
    index = ord(word[i]) # 아스키 코드로 변경
    index = index - 65 # 배열 인덱스 0부터 설정
    alphabet[index] += 1 # 존재하면 1 증가

biggest = max(alphabet) # 알파벳 리스트 최댓값
count = 0
for i in range(len(alphabet)):
    if alphabet[i] == biggest: # 최댓값 개수
        count += 1

if count > 1: # 최댓값이 여러 개 존재하는 경우
    print("?")
else:
    index = alphabet.index(max(alphabet)) # 최댓값의 인덱스
    num = index + 65 # 65 더해서 원래의 아스키 코드 값으로
    print(chr(num)) # 아스키 코드 값을 문자로 변환