n = input() #문자열로 숫자를 입력받는다.

array = [] #숫자를 담을 리스트 선언
for i in n: #입력받은 문자열 n의 각각의 문자 i에 접근 ex) "12345" -> "1","2","3","4","5"
    array.append(int(i)) #i를 int형태로 바꾸어 리스트에 원소로 추가

array.sort(reverse=True) # 숫자를 내림차순으로 정렬

for i in array: #배열의 각 원소에 접근
    print(i,end='') #각 원소를 빈칸없이 출력