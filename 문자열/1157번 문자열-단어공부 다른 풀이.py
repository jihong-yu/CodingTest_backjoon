word = input()
word = word.upper()  # 입력받은 문자를 대문자로 변경
result = []  # 등장하는 문자를 저장할 리스트 선언
max_count = []  # 등장하는 문자의 횟수를 저장할 리스트 선언

for i in set(word):  # 문자열의 중복을 우선 없애주고 반복문을 돈다
    result.append(i)  # result 리스트에 문자열 i를 추가해준다.
    max_count.append(word.count(i))  # 문자열 i를 추가한 뒤에 해당하는 문자열의 개수를 max_count리스트에 추가해준다.

if max_count.count(max(max_count)) >= 2:  # 만약 max_count리스트에 저장되어 있는 최대값이 2개 이상이라면
    print("?")  # ?를 출력
else:  # 만약 저장되어 있는 최대값이 1개라면
    print(result[max_count.index(max(max_count))])
    # max_count리스트에 저장되어 있는 해당 최대값의 인덱스값을 찾아서 result의 인덱스로 적용시켜 출력한다.
