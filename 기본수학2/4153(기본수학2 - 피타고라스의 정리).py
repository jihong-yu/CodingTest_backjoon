while True:
    array1 = list(map(int,input().split())) #리스트의 형태로 받는다.
    if array1.count(0) == 3: #0이 3개이면 반복문 탈출
        break
    maxNum = max(array1) #최대값을 따로 변수에 저장
    array1.remove(maxNum) #그 최대값을 배열에서 제거

    array1.sort() #오름차순으로 정리
    if array1[2] ** 2 == array1[0] ** 2 + array1[1] ** 2: #피타고라스의 방정식이 성립한다면
    #if maxNum ** 2 == array1[0] ** 2 + array1[1] ** 2: #피타고라스의 방정식이 성립한다면
        print("right") #right출력
    else: #그렇지않다면
        print("wrong") #wrong출력

