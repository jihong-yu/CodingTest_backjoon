n = input()

array = list(map(ord, n)) # 입력받은 문자열을 아스키코드로 변환
array2 = [-1] * (ord("z") - ord("a") + 1) # 해당문자열이 존재하는 위치를 담을 배열 선언

index = 0 # array2에 이용할 index값 생성
for i in range(ord("a"), ord("z") + 1): # a - z 까지 돌기위한 반복문 설정
    for j in range(array.__len__()): #각각의 문자(a-z) 가 입력받은 문자열의 어디에 위치하는지 해당 위치값을 찾기위한 반복문설정
        if i == array[j]: # 만약 a - z 의 문자가 해당 문자열 내부에 존재한다면
            array2[index] = j #그 위치값을 array2의 배열의 위치에 담아준다음
            break # break 가 없다면 같은 문자가 나오면 그 뒤에값이 저장되기 때문에 앞에값만 저장하기 위해서 break 걸어주기
    index += 1 # a = 0, b = 1 , c = 2 와 같이 array2 리스트에 index를 설정해주기 위해 각각의 문자의 반복문이 끝났다면 index에다가 +1 해주기

for i in array2:
    print(i,end=" ") #array2 값 출력