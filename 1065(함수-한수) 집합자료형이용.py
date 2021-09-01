def hansu(x: int):
    count = 0 #개수

    for i in range(1, x + 1):
        array = list(map(int, str(i))) #숫자를 문자열로 변환후 리스트에 넣으면 각각의 원소만 저장이가능하다. 이를 map함수를 이용해 각각의 원소를 다시 int형을 바꾸어 준다.
        if i > 99: #세자리수 이상일때의 계산
            difference = set([])  # 중복값을 허용안하는 집합자료형 set자료형으로 설정
            for j in range(1, array.__len__()):
                difference.add(array[j] - array[j - 1]) #중복을 허용하지 않기 때문에 만약 앞원소와 뒤의원소의 차가 같다면 계속해서 똑같은 원소가 삽입이 되지 않는다.
            if difference.__len__() == 1: #즉, 자리수 차 값이 똑같다는 것은 집합자료형 길이가 1인것과 마찬가지
                count += 1 #그럴때 개수에 +1 해주기
        else: #두자리수 미만일때는 그냥 개수에다가 +1 해주기
            count += 1
    print(count)

n = int(input())
hansu(n)
