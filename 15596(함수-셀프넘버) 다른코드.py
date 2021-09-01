def d(n) -> int:
    temp = 0  # 각자리수를 더하기 위한 변수 생성
    for x in list(
            str(n)):  # 숫자나 문자를 String 형식으로 list에 담을 경우 각각의 자리수(각각의문자)가 원소로 담김 ex:"abc" -> "a","b","c" ,"123" -> "1","2","3"
        temp = temp + int(x)  # 각자리수를 더해주어 a에 대입
    return n + temp  # 전체수와 각자리수를 더함


array = []
for i in range(1, 10001):
    k = d(i)  # 각자리수+전체수를 더하는 함수를 호출하여 k에 대입
    array.append(k)  # k값을 array리스트에 삽입(생성자가 있는 값들만 삽입)

for b in range(1, 10001):
    if b in array:  # array리스트에 b값이 있으면 넘김
        pass  # 아무것도 안한다.
    else: #없는것들 즉, 생성자가 없는 숫자만 출력
        print(b)  # b값 출력
