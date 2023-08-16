nums = input() # 남은 수를 이어 붙인 수를 문자열로 입력받음
i = 0 # 비교할 수
while True:
    i += 1 # 1부터 시작
    num = str(i) # 수를 문자열로 반환

    while len(num) > 0 and len(nums) > 0: # 두 문자열의 길이가 0보다 크다면
        if num[0] == nums[0]: # 같은 수라면
            nums = nums[1:] # nums의 첫 숫자 삭제
        num = num[1:] # num의 첫 숫자 삭제
    if nums == '': # nums가 빈 문자열이라면
        print(i) # 그때의 수 출력
        break