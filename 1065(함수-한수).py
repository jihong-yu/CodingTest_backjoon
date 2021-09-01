def hansu(x: int):
    count = 0 #개수
    for i in range(1, x + 1):
        array = list(map(int, str(i))) #숫자를 문자열로 변환후 리스트에 넣으면 각각의 원소만 저장이가능하다. 이를 map함수를 이용해 각각의 원소를 다시 int형을 바꾸어 준다.
        if i > 99: #세자리수일때의 계산
            if array[1] - array[0] == array[2] - array[1]:
                count += 1
        elif i > 999: #네자리 수일때의 계산
            if array[1] - array[0] == array[2] - array[1] == array[3] - array[2]:
                count += 1
        else: #두자리수 미만일때는 그냥 count에다가 +1 해주기
            count += 1
    print(count)


n = int(input())
hansu(n)
